# Video Streaming Bot Design

## Overview

Implement a video streaming bot that stream videos randomly similar to human activity which can be used for applications such as traffic generation in a test environment. Such bots can be configured to meet users&#39; demand but scaling up the number of bots and customizing the length of time to stream.

## Objective

To design and build a system that is able to automatically create instances of bots that are able to scrape for video links and organize into playlists then stream the videos according to users configuration. 
It can also support many user friendly features as mentioned in the features section below.

## Design

The video streaming bot design consists of 3 functions namely System Pro, Video-Bot and Video-Play. System-Pro will provide the provisioning to create instances of the Video-Bot which will scrape for video links from a predefined website for Video-Play to stream the videos.

![VideoStreamingBot-Design](https://github.com/TIC4302/video-streaming-bot/blob/master/doc/images/VideoStreamDesign-Page-1.jpg)

Figure 1

![VideoStreamingBot](https://github.com/TIC4302/video-streaming-bot/blob/master/doc/images/VideoStreamDesign-Page-2.jpg)

Figure 2. 
Each swimlane indicate 4 different parts of workflow, the first section of the workflow is based on user&#39;s interaction, follow by provisioning workflow according to user&#39;s requirement, design and execution (either using lightweight Docker/Kubernetes solution, or Vagrant/Virtualbox combination, the third section is the actual play or execution of the video streaming bot. The final section is all these activities are recorded as network statistics.

## Features

We have identified the following features for the video streaming bots:

1. The bots should be able to scrape websites automatically for video URLs and store them into playlists.
2. We can set the bots to play the videos sequentially or randomly from the playlist. We can store the playlists and restore them to play at a later time.
3. The length of videos will be randomized in the playlist.and they will play from start to end.
4. The bots will automatically close the browser after a video has finished with the streaming and then proceed to play the next video in a new browser window.
5. The system can make use of provided api by various video streaming platforms to play the videos
6. Users can define the number of bots to run, up to a maximum of 8 bots playing simultaneously.
7. Users can specify the duration for the bots to run. For e.g. to play for 4 hours even though the playlist may be longer.

We have identified the following Web browser features that can be perform by the bots

1. The bots can login to Youtube and simulate scrolling and pausing through the page.
2. The bots will stream the video through web browsers.

The system will have the following features for provisioning:

1. Users will be able to provision images using VM/Dockers
2. Users can choose how many containers/VMs to run

The system will have the following error-recovery features:

1. Bots will automatically go to the next video if the current video freezes/cannot play or the website encounters errors.

## Implementation

This project will be implemented by using Python, Selenium framework for its bots. Automatic provisioning tools such as Docker, Kubernetes, Ansible, Vagrant and Virtualbox will be used to dynamically provision specific numbers of container instances according to users&#39; needs for a start.

Such dynamic provisioning can be adopted by its user based on the hardware infrastructure capabilities the user is having.

A nice to have feature will be to provide network traffic monitoring information using vnStat and or other tools to record and log this traffic to give the user the idea of the network traffic and bandwidth utilization in real time.

## Consideration

Hardware requirement to run the bots

Hardware needs to scale with the number of bots.

Support multiple platforms

Bots can be run on different streaming websites.

How can users report bugs to the dev team

Provides a channel to receive and respond to bug reports.

Providing a feedback avenue for users.

Feedback can range from improvement suggestions to request for additional features..

Future enhancements

Generating report on bots execution such as number of video played, length of videos, failed attempts, etc.

The bot needs to behave as human-like as possible to prevent websites from detecting it as a bot and thus blocking the bot&#39;s IP address.
