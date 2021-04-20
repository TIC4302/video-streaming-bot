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
Step 5: Check Docker Version

```console
$ docker --version
```
Step 6: Build with the Docker file

Restart your machine. Create a folder and download the docker file and youtube_bot.py from Operation folder into the newly created folder and run this command
```console
$ docker build . -t videobot:1
```
