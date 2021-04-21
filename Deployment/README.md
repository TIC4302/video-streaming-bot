## Docker Deployment Guide
This has been tested in Ubuntu 20.04

Step 1: Update APT

```console
$ sudo apt update
$ sudo apt upgrade
```
Step 2: Download and Install Docker

```console
$ sudo apt install docker.io
```
Step 3: Launch Docker

```console
$ sudo systemctl enable --now docker
```
Step 4: Set User Privileges

```console
$ sudo usermod -aG docker yourname
```
Step 5: Check Docker Version and restart your machine.

```console
$ docker --version
```
Step 6: Clone from Github

Clone this repository to the current local directory
```console
$ git clone https://github.com/TIC4302/video-streaming-bot.git
```
Step 7: Build with the Bash Script

Go into video-streaming-bot folder, set the script with executable permission and run the script
```console
$ chmod +X build.sh
$ ./build.sh
```

