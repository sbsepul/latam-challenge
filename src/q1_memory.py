from typing import List, Tuple
from datetime import datetime

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    start_time = time.time()

    tweet_counts = {}
    user_counts = {}

    with open(file_path, "r") as file:
        for line in file:
            tweet = json.loads(line)
            date = datetime.strptime(tweet["tweet_date"], "%Y-%m-%d").date()
            user = tweet["username"]

            if date not in tweet_counts:
                tweet_counts[date] = 0
                user_counts[date] = {}
            tweet_counts[date] += 1

            if user not in user_counts[date]:
                user_counts[date][user] = 0
            user_counts[date][user] += 1

    top_dates = sorted(tweet_counts, key=tweet_counts.get, reverse=True)[:10]
    result = [
        (date, max(user_counts[date], key=user_counts[date].get)) for date in top_dates
    ]

    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")

    return result
