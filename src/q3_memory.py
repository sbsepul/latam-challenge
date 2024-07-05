import json
import time
from collections import Counter
from typing import List, Tuple

import memory_profiler


@memory_profiler.profile
def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    start_time = time.time()

    mentions_counts = Counter()

    with open(file_path, "r") as file:
        for line in file:
            tweet = json.loads(line)
            mentions = tweet.get("mentions")
            if mentions:
                mention_list = mentions.split(",")
                mentions_counts.update(mention_list)

    top_10_mentions = mentions_counts.most_common(10)

    result = [(mention, count) for mention, count in top_10_mentions]
    end_time = time.time()

    print(f"Execution time: {end_time - start_time} seconds")

    return result
