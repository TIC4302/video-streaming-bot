FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install firefox -y && apt-get install xauth -y
RUN apt-get install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update && apt-get install python3.8 -y && apt install -y python3-pip
RUN apt install -y build-essential libssl-dev libffi-dev python3-dev
RUN apt install -y python3-venv
RUN pip3 install youtube_dl
RUN pip3 install pafy
RUN pip3 install python-vlc
#RUN DEBIAN_FRONTEND=noninteractive apt-get install vlc -y

RUN apt-get install -y --no-install-recommends \
		ca-certificates \
		libgl1-mesa-dri \
		libgl1-mesa-glx \
		pulseaudio \
		alsa-utils \
		dbus* \
		vlc && \
	apt-get -y -f install && \
	useradd -m vlc && \
	usermod -a -G audio,video vlc && \
	rm -rf /var/lib/apt/lists/*

ADD play_video.py /home/play_video.py
COPY . .
CMD ["/home/play_video.py"]

USER vlc

#WORKDIR /home/vlc/media

#ENTRYPOINT ["vlc", "--no-qt-privacy-ask", "--no-metadata-network-access", "--snapshot-path=/home/vlc/snapshots"]
ENTRYPOINT ["python3"]
#COPY init-script.bash /opt/program/init-script.bash
#ENTRYPOINT /opt/program/init-script.bash && /usr/bin/firefox
