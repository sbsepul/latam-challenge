import time
from datetime import datetime
from typing import List, Tuple

from google.cloud import bigquery
import os

PROJECT_ID = os.getenv("PROJECT_ID")
DATASET_ID = os.getenv("DATASET_ID")
TABLE_ID = os.getenv("TABLE_ID")


def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    start_time = time.time()

    bigquery_client = bigquery.Client()

    # Realizar consulta en BigQuery
    query = """
    SELECT DATE(date) as tweet_date, username, COUNT(*) as tweet_count
    FROM `{project_id}.{dataset_id}.{table_id}`
    GROUP BY date, username
    ORDER BY tweet_count DESC
    LIMIT 10
    """.format(project_id=PROJECT_ID, dataset_id=DATASET_ID, table_id=TABLE_ID)

    query_job = bigquery_client.query(query)
    results = query_job.result()

    result = [(row.tweet_date, row.username) for row in results]

    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")

    return result
