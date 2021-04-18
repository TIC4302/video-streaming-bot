## Youtube-bot User Guide

### User guide

The bot will take in 2 parameters:

1. search query : this is the query to search for videos on Youtube website.
2. number of webpages : this is the number of webpages to search based on the search query.

For example, the following means to search and scrap video links from 5 webpages of "hacking" query :

```console
$ python3 youtube_bot.py hacking 5
```

To terminate the bot, type in the command :

```console
[ctrl]+c
```

### Bot behaviour

1. Bot will run on an infinite loop until terminated by user.
2. Bot will collect a list of video links based on the search query.
3. The list of video links collected will be randomized each time before repeating.
4. Each video playtime will be randomized between 5sec to 20sec.
5. Bot will display the list of randomised video on the terminal.
6. Bot will display the video title, url, actual and randomised playtime information on the terminal.
7. Bot will access each video urls and let the video play for the lenght of randomised playtime, headlessly.
