import os

import emoji
import memory_profiler
import pandas as pd


def extract_emojis(text):
    emojis = emoji.distinct_emoji_list(text)
    return ",".join(emojis) if emojis else None


def extract_mentions(mentions):
    if not mentions:
        return None
    else:
        users = [user["username"] for user in mentions]
        return ",".join(users) if users else None


@memory_profiler.profile
def preprocess_twitter_data(file_path):
    data = pd.read_json(file_path, lines=True)
    filtered_data = data[["date", "user", "content", "mentionedUsers", "id"]]
    filtered_data["username"] = filtered_data["user"].apply(lambda x: x["username"])
    filtered_data["emojis"] = filtered_data["content"].apply(extract_emojis)
    filtered_data["mentions"] = filtered_data["mentionedUsers"].apply(extract_mentions)
    filtered_data.drop(columns=["user", "mentionedUsers"], inplace=True)
    filtered_data.rename(columns={"id": "tweet_id", "date": "tweet_date"}, inplace=True)
    filtered_data["tweet_date"] = pd.to_datetime(filtered_data["tweet_date"]).dt.date
    filtered_data["tweet_date"] = filtered_data["tweet_date"].apply(
        lambda x: x.strftime("%Y-%m-%d")
    )

    basename = os.path.basename(file_path)
    basename = basename.split(".")[0]
    filtered_name = f"{basename}_filtered.json"

    filtered_data.to_json(filtered_name, orient="records", lines=True)


if __name__ == "__main__":
    preprocess_twitter_data("farmers-protest-tweets-2021-2-4.json")
