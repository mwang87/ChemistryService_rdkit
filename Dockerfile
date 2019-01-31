FROM mcs07/rdkit:latest

MAINTAINER Mingxun Wang "mwang87@gmail.com"

RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip3 install flask
RUN pip3 install gunicorn
RUN pip3 install requests

COPY . /app
WORKDIR /app
