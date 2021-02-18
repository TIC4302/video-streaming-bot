FROM ubuntu:latest
RUN apt-get update && apt-get install firefox -y && apt-get install xauth -y
#RUN apt-get install xauth -y

COPY init-script.bash /opt/program/init-script.bash

ENTRYPOINT /opt/program/init-script.bash && /usr/bin/firefox
