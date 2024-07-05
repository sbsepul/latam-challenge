import time
from collections import Counter
from typing import List, Tuple

import pandas as pd


def q2_time(file_path: str) -> List[Tuple[str, int]]:
    start_time = time.time()

    data = pd.read_json(file_path, lines=True)
    data["emojis"] = data["emojis"].apply(lambda x: x.split(",") if x else [])
    emoji_counts = Counter()
    for emojis in data["emojis"]:
        emoji_counts.update(emojis)

    top_10_emojis = emoji_counts.most_common(10)
    result = [(emoji, count) for emoji, count in top_10_emojis]
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")
    return result
