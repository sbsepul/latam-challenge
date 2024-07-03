import pandas as pd
import emoji
import memory_profiler


def extract_emojis(text):
    emojis = emoji.distinct_emoji_list(text)
    return ",".join(emojis) if emojis else None


def extract_mentions(mentions):
    if not mentions:
        return None
    else:
        users = [user["username"] for user in mentions]
        return ",".join(users) if users else None


@memory_profiler.profile
def preprocess_twitter_data(file_path):
    data = pd.read_json(file_path, lines=True)
    filtered_data = data[["date", "user", "content", "mentionedUsers", "id"]]
    filtered_data["username"] = filtered_data["user"].apply(lambda x: x["username"])
    filtered_data["emojis"] = filtered_data["content"].apply(extract_emojis)
    filtered_data["mentions"] = filtered_data["mentionedUsers"].apply(extract_mentions)
    filtered_data.drop(columns=["user", "mentionedUsers"], inplace=True)
    filtered_data.rename(columns={"id": "tweet_id", "date": "tweet_date"}, inplace=True)

    # Guardar el DataFrame filtrado en un nuevo archivo CSV
    filtered_data.to_csv("filtered_data.csv", index=False)

    print("Preprocessing completed and data saved to filtered_data.csv successfully.")


preprocess_twitter_data("farmers-protest-tweets-2021-2-4.json")
