FROM alpine:latest
FROM python:3.7

RUN apt-get update -y && \
	apt-get install -y python-pip python-dev

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

Expose 5000
