FROM ubuntu:latest as builder

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
RUN apt update
RUN apt upgrade -y
RUN apt install wget -y
RUN pip3 install pandas
RUN pip3 install selenium
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.29.0/geckodriver-v0.29.0-linux64.tar.gz
RUN tar xzf geckodriver-v0.29.0-linux64.tar.gz
RUN mv geckodriver /usr/bin/
RUN chown root:root /usr/bin/geckodriver
RUN chmod +x /usr/bin/geckodriver
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

ADD ../Operation/youtube_bot.py /home/youtube_bot.py
COPY . .
USER vlc
#CMD ["bash"] #uncomment if want to use bash in docker for troubleshooting
CMD ["/home/youtube_bot.py"] 
ENTRYPOINT ["python3"]

