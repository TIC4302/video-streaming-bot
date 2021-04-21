#! /bin/sh
cp Deployment/Dockerfile .
cp Operation/youtube_bot.py .
docker build . -t videbot:1
