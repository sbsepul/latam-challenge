import time
from datetime import datetime
from typing import List, Tuple

import pandas as pd


def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    start_time = time.time()

    data = pd.read_json(file_path, lines=True)

    data["tweet_date"] = pd.to_datetime(data["tweet_date"]).dt.date
    top_dates = data.groupby("tweet_date").size().nlargest(10).index
    result = []

    for date in top_dates:
        top_user = data[data["tweet_date"] == date]["username"].value_counts().idxmax()
        result.append((date, top_user))

    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")

    return result
