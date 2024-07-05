import json
import time
from collections import Counter
from typing import List, Tuple

import memory_profiler


@memory_profiler.profile
def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    start_time = time.time()

    emoji_counts = Counter()

    with open(file_path, "r") as file:
        for line in file:
            tweet = json.loads(line)
            emojis = tweet.get("emojis")
            if emojis:
                emoji_list = emojis.split(",")
                emoji_counts.update(emoji_list)

    top_10_emojis = emoji_counts.most_common(10)
    result = [(emoji, count) for emoji, count in top_10_emojis]

    end_time = time.time()

    print(f"Execution time: {end_time - start_time} seconds")

    return result


if __name__ == "__main__":
    q2_memory("farmers-protest-tweets-2021-2-4_filtered.json")
