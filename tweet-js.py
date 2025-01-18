#!/usr/bin/python3
import datetime
import json
import pytz
import os
from dateutil.parser import parse
from argparse import ArgumentParser
# import pandas as pd

utc = pytz.UTC


def read_twitter_json(file_name):
    """Reads JSON file and returns a JSON object."""
    if not os.path.exists(file_name):
        raise FileNotFoundError(f"File not found: {file_name}")
    try:
        with open(file_name, "r", encoding="utf8") as tweets_file:
            tweets_lines = tweets_file.readlines()
        if tweets_lines:
		    # Remove custom header
            tweets_lines[0] = tweets_lines[0].replace('window.YTD.tweets.part0 = ', '')

        # Convert list back to text
        tweets_data = ''.join(tweets_lines)

        # Parse JSON twitter data
        tweets_js = json.loads(tweets_data)
        return tweets_js

    except json.JSONDecodeError as e:
        raise ValueError(f"Error decoding JSON: {e}\nCheck input file contents.")


def tweet_decode(tweet):
    """Extracts and simplifies tweet data."""
    # Get data from tweet
    tweet_simple = {
        'full_text': tweet['tweet'].get('full_text', ''),
        'created_at': tweet['tweet'].get('created_at', '')
    }

	# Parse date to datetime
    tweet_simple['datetime'] = parse(tweet_simple['created_at'])

    # Process hashtags
    tweet_simple['hashtags'] = [tag['text'] for tag in tweet['tweet']['entities'].get('hashtags', [])]
    # Process URLs
    tweet_simple['urls'] = [url['expanded_url'] for url in tweet['tweet']['entities'].get('urls', [])]

    return tweet_simple


# Argument parsing
parser = ArgumentParser(description="Filter and process Twitter JSON data.")
parser.add_argument("-f", "--file", required=True, help="Path to Twitter JSON archive.", metavar="FILENAME")
parser.add_argument("-t", "--hashtag", help="Filter by hashtag", metavar="HASHTAG")
parser.add_argument("-s", "--date-start", help="Start Date", metavar="START_DATE")
parser.add_argument("-e", "--date-end", help="End Date", metavar="END_DATE")
parser.add_argument("-g", "--list-hashtags", action="store_true", help="List the hashtags")
parser.add_argument("-x", "--skip-retweets", action="store_true", help="Skip retweets")

args = parser.parse_args()

# Validate and parse dates
date_start = utc.localize(parse(args.date_start)) if args.date_start else None
date_end = utc.localize(parse(args.date_end)) if args.date_end else None

# Read Twitter file
tweets_js = read_twitter_json(args.file)

# Sort it by date
tweets_js = sorted(tweets_js, key=lambda x: parse(x['tweet']['created_at']))

# Process tweets

# Variable initialization
outs = []      # This will be a list of post dictionaries
hashtags = set()

# Loop over tweets
for tweet in tweets_js:
    # Do Skip re-tweets?
    if args.skip_retweets and tweet['tweet']['full_text'].startswith("RT @"):
        continue

    # Decode tweet in a simple structure
    tweet_simple = tweet_decode(tweet)

    # Will these two cause an error if there is no date_start?!
    if date_start and tweet_simple['datetime'] <= date_start:
        continue
    if date_end and tweet_simple['datetime'] >= date_end:
        continue

    if args.hashtag:
        # Filter by hashtag
        if args.hashtag in tweet_simple['hashtags']:
            outs.append(tweet_simple)
    elif args.list_hashtags:
        hashtags.update(tweet_simple['hashtags'])
    else:
        outs.append(tweet_simple)

# List hashtags
if args.list_hashtags:
    for tag in sorted(hashtags):
        print(tag)


# print(f"\"\"\"{tweet['full_text']}\"\"\"")

# df = pd.DataFrame(outs)
# print(
#     df.head().to_markdown()
# )

# outs.reverse()   # Newer tweets first

print(
    *[tweet['full_text'] for tweet in outs],
    sep="\n\n\n-----\n\n\n"
)

