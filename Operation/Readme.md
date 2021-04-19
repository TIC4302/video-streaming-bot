## Youtube-bot User Guide

### User guide

The bot will take in 2 parameters:

1. search query : this is the query to search for videos on Youtube website.
2. number of webpages : this is the number of webpages to search based on the search query.

For example, the following means to search and scrap video links from 5 webpages of "hacking" query :

```console
$ python3 youtube_bot.py hacking 5
```
If you do  not want to specify anything. Just enter this command:

```console
$ sudo docker run -it videobot:1
```

To terminate the bot, type in the command :

```console
[ctrl]+c
```

### Bot behaviour

1. Bot will run on an infinite loop until terminated by user.
2. Bot will collect a list of video urls based on the search query.
3. The list of video urls collected will be randomized each time before repeating.
4. Each video playtime will be randomized between 5sec to 20sec.
5. Bot will display the list of randomized video title, url, playtime time and randomized playtime on the terminal.
6. Bot will display each video title, url, actual and randomized playtime information on the terminal.
7. Bot will access each video urls and let the video play for the length of randomized playtime, headlessly.
