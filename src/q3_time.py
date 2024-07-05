import time
from collections import Counter
from typing import List, Tuple

import pandas as pd


def q3_time(file_path: str) -> List[Tuple[str, int]]:
    start_time = time.time()

    data = pd.read_json(file_path, lines=True)
    data["mentions"] = data["mentions"].apply(lambda x: x.split(",") if x else [])
    mentions_counts = Counter()
    for mentions in data["mentions"]:
        mentions_counts.update(mentions)

    top_10_mentions = mentions_counts.most_common(10)
    result = [(mention, count) for mention, count in top_10_mentions]
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")

    return result
