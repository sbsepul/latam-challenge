import time
from datetime import datetime
from typing import List, Tuple

import pandas as pd
from google.cloud import bigquery, storage


def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    start_time = time.time()

    storage_client = storage.Client()
    bigquery_client = bigquery.Client()

    # Descargar el archivo desde Cloud Storage
    bucket_name, blob_name = file_path.split("/", 1)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.download_to_filename("/tmp/jsonfile.json")

    # Cargar datos en un DataFrame
    data = pd.read_json("/tmp/jsonfile.json", lines=True)
    data["date"] = pd.to_datetime(data["date"]).dt.date

    # Subir datos a BigQuery
    dataset_id = "your_dataset_id"
    table_id = "your_table_id"
    table_ref = bigquery_client.dataset(dataset_id).table(table_id)

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
        autodetect=True,
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
    )

    with open("/tmp/jsonfile.json", "rb") as source_file:
        job = bigquery_client.load_table_from_file(
            source_file, table_ref, job_config=job_config
        )

    job.result()

    # Realizar consulta en BigQuery
    query = """
    SELECT DATE(date) as tweet_date, user.username, COUNT(*) as tweet_count
    FROM `your_project_id.your_dataset_id.your_table_id`
    GROUP BY tweet_date, user.username
    ORDER BY tweet_count DESC
    LIMIT 10
    """

    query_job = bigquery_client.query(query)
    results = query_job.result()

    result = [(row.tweet_date, row.username) for row in results]

    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")

    return result


# Probar la función
file_path = "your-bucket-name/path/to/jsonfile.json"
result = q1_time(file_path)
print(result)
