**Docker Deployment**

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
Step 6: Build wwith the Docker file

Downlaod the docker file and run this command
```console
$ docker build . -t videobot:1
```
