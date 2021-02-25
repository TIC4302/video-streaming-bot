FROM ubuntu:latest
RUN apt-get update && apt-get install firefox -y && apt-get install xauth -y
RUN apt-get install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update && apt-get install python3.8 -y && apt install -y python3-pip
RUN apt install -y build-essential libssl-dev libffi-dev python3-dev
RUN apt install -y python3-venv

#COPY init-script.bash /opt/program/init-script.bash
#ENTRYPOINT /opt/program/init-script.bash && /usr/bin/firefox