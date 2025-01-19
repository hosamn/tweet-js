# tweet-js.py #

A simple Python parser for Twitter JSON archive, aka `tweets.js`.


## Usage ##

- Download this app and extract or git clone it.
- Download your Twitter archive from [This Link](https://x.com/settings/download_your_data) and extract.
- Note the path to `tweets.js`, maybe copy it to app directory.
- To print all the tweets, Run:

```
python tweet-js.py -f tweets.js
```

## Options ##

| Option | Long Option | Description |
| - | - | - |
| `-f` | `--filename` | Path to Twitter JSON archive tweets.js |
| `-t` | `--text-search` | Text string to search for |
| `-#` | `--hashtag` | Filter by hashtag |
| `-l` | `--list-hashtags` | List the hashtags |
| `-s` | `--date-start` | Start Date |
| `-e` | `--date-end` | End Date |
| `-x` | `--skip-retweets` | Skip Retweets |

## Tests ##

    To test the app, place `tweets.js` in the same directory and run `./test`
    you might need to set executable flag using `chmod +x ./test`
    
    This will run a collection of commands to test app execution
    and will produce a set of ouput text files in the same directory.

    You can edit the file to get more relevant results and
    you can also check the file's contents for more usage examples.


## Examples ##

### Search for text ###

To get tweets that contain a certain text string:

```
python tweet-js.py -f tweets.js -t "search_text"
```


### Filter By Hashtag ###

To print tweets with a specific hashtag:

```
python tweet-js.py -f tweets.js -# "hashtag"
```


### Filter By Date ###

The `-s` argument filters tweets by start date and `-e` by end date. You can use them together:

```
python tweet-js.py -f tweets.js -s "2019-01-01" -e "2020-01-01"
```

### Extract Hashtags ###

To get a list of all used hashtags:

```
python tweet-js.py -f tweets.js -l
```


### Skip Retweets ###

```
python tweet-js.py -f tweets.js -x
```
