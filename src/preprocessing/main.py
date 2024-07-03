from google.cloud import storage
import pandas as pd
import json
import emoji
import logging
import traceback

def try_catch_log(wrapped_func):
  def wrapper(*args, **kwargs):
    try:
      response = wrapped_func(*args, **kwargs)
    except Exception:
      # Replace new lines with spaces so as to prevent several entries which
      # would trigger several errors.
      error_message = traceback.format_exc().replace('\n', '  ')
      logging.error(error_message)
      return 'Error';
    return response;
  return wrapper;

@try_catch_log
def preprocess_twitter_data(event, context):
    def extract_emojis(text):
        emojis = emoji.distinct_emoji_list(text)
        return ",".join(emojis) if emojis else None

    def extract_mentions(mentions):
        if not mentions:
            return []
        else:
            users = [user['username'] for user in mentions]
            return ",".join(users) if users else None
    
    storage_client = storage.Client()

    bucket_name = event['bucket']
    file_name = event['name']

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_name)
    blob.download_to_filename('/tmp/jsonfile.json')

    data = pd.read_json('/tmp/jsonfile.json', lines=True)

    filtered_data = data[['date', 'user', 'content', 'mentionedUsers', 'id']]
    filtered_data['username'] = filtered_data['user'].apply(lambda x: x['username'])
    filtered_data['emojis'] = filtered_data['content'].apply(extract_emojis)
    filtered_data['mentions'] = filtered_data['mentionedUsers'].apply(extract_mentions)
    filtered_data.drop(columns=['user', 'mentionedUsers'], inplace=True)
    
    # Guardar el DataFrame filtrado en un nuevo archivo CSV
    filtered_data.to_csv('/tmp/filtered_data.csv', index=False)
    
    # Subir el archivo CSV filtrado de vuelta a Cloud Storage
    output_blob = bucket.blob('filtered/filtered_data.csv')
    output_blob.upload_from_filename('/tmp/filtered_data.csv')

    print("Preprocessing completed and data uploaded to Cloud Storage successfully.")
