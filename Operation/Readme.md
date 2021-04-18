## Youtube-bot User Guide

### User guide

The bot will take in 2 parameters:

1. search query : this is the query to search Youtube videos.
2. number of webpages : this is the number of webpages to search based on the search query.

For example, the following would mean to search for 5 webpages of "hacking" videos :

```console
$ python3 youtube_bot.py hacking 5
```

To terminate the bot, type in the command :

```console
[ctrl]+c
```



This is required Docker to run locally for verification before push to the Docker Hub. Install with these following commands:

```console
ncl@orchestrator:~/$ sudo apt-get update
ncl@orchestrator:~/$ sudo apt-get install docker-ce docker-ce-cli containerd.io
ncl@orchestrator:~/$ sudo docker run hello-world
``` 
The detail steps can be found in this [link](https://docs.docker.com/install/linux/docker-ce/ubuntu/).

### Download the Source Code
 
Download the whole source code of OctoBot software from the GitHub.
