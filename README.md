# tweet-js.py #

A simple Python parser for Twitter JSON archive, aka `tweets.js`.


## Usage ##

- Download your Twitter archive file from [This Link](https://x.com/settings/download_your_data)
- Uncompress it.
- Check the path to the file tweets.js.
- Execute the parser:

```
python tweet-js.py -f tweets.js
```

This will print the content of all tweets.

## Filter by hashtag ##

```
python tweet-js.py -f tweet.js -t hashtag
```

This will print the content of the tweets with this hashtag.


## Filter by date ##

The `-s` argument filters messages by start date and `-e` argument filters messages by end date. They can be used together:

```
python tweet-js.py -f tweet.js -s 2019-01-01 -e 2020-01-01
```

