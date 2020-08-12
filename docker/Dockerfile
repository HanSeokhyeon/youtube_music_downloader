FROM        python:3.7
MAINTAINER	sah0322@naver.com

RUN     apt-get -y update && apt-get -y install ffmpeg curl
RUN     curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
RUN     chmod a+rx /usr/local/bin/youtube-dl

RUN     pip install --upgrade pip
RUN     pip install numpy pandas

WORKDIR		/opt/project