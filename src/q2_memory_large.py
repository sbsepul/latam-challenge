import json
import time
from collections import Counter
from typing import List, Tuple

import emoji
import memory_profiler


def extract_emojis(text: str):
    """
    Extract emojis from the text
    @param text: str
    @return: str
    """
    emojis = emoji.distinct_emoji_list(text)
    return ",".join(emojis) if emojis else None


@memory_profiler.profile
def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    start_time = time.time()

    emoji_counter = Counter()

    with open(file_path, "r") as file:
        for line in file:
            tweet = json.loads(line)
            if tweet.get("content") is None:
                continue
            emojis = extract_emojis(tweet.get("content"))
            if emojis:
                emoji_list = emojis.split(",")
                emoji_counter.update(emoji_list)
    result = emoji_counter.most_common(10)

    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")

    return result
