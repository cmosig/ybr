# YBR

YBR is a better recomendation service for youtube. You can subscribe to a series (regex) on a channel. 
When fetching (-f) your series, only the ones you haven't watched will be added to the "new episodes list" (nel).
This way you will not get distracted from other videos that may be cool, but you actually did not plan to watch...

## Installation

git clone and run setup.py

## Usage
After installation run: _ybr --initDB_
This will initialize the database. After this function has been called once, it has no further effect when called again.
Provide channelname and a regex matching the videos titles you want to watch using: _ybr --add-series -s regey -c channel_
Fetch the series using _ybr -f_ and display results using _ybr -p_. You can remove watched titles by index using _ybr -rn int_
Read _ybr -h_ for other functions.

## License
[MIT](https://choosealicense.com/licenses/mit/)
