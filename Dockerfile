FROM ubuntu:16.04

## Install pip
RUN apt-get update && \
    apt-get install -y python3-pip && \
    pip3 install --upgrade pip

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app
# Copy the current files to the docker's folder
COPY . /usr/src/app

# Libraries
RUN pip install --process-dependency-links -e .

ENTRYPOINT python3 main.py