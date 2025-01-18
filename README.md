# tweet-js.py #

A simple Python parser for Twitter JSON archive, aka `tweets.js`.


## Usage ##

- Download your Twitter archive from [This Link](https://x.com/settings/download_your_data)
- Uncompress it and check the path to `tweets.js`.
- Print all the tweets:

```
python tweet-js.py -f tweets.js
```


## Filter by hashtag ##

```
python tweet-js.py -f tweet.js -t hashtag
```

This will print the content of the tweets with this hashtag.


## Filter by date ##

The `-s` argument filters messages by start date and `-e` by end date. They can be used together:

```
python tweet-js.py -f tweet.js -s 2019-01-01 -e 2020-01-01
```

## Extract Hashtags ##

```
python tweet-js.py -g -f tweets.js > hashtags.txt
```


## Skip Retweets ##

```
python tweet-js.py -x -f tweets.js > original_tweets.txt
```


## Options ##

| Option | Long Option | Description |
| - | - | - |
| `-f` | `--file` | Path to Twitter JSON archive  `tweets.js` |
| `-t` | `--hashtag` | Filter by hashtag |
| `-g` | `--list-hashtags` | List the hashtags |
| `-s` | `--date-start` | Start Date |
| `-e` | `--date-end` | End Date |
| `-x` | `--skip-retweets` | Skip Retweets |
