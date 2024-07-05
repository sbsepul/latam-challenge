import json
import time
from collections import Counter
from typing import List, Tuple

import memory_profiler


@memory_profiler.profile
def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    start_time = time.time()

    mention_counter = Counter()

    with open(file_path, "r") as file:
        for line in file:
            tweet = json.loads(line)
            if tweet["mentionedUsers"]:
                mentions = [user["username"] for user in tweet["mentionedUsers"]]
                mention_counter.update(mentions)

    result = mention_counter.most_common(10)

    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")

    return result
