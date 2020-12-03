FROM jfloff/alpine-python:latest

RUN apk update --no-cache && apk upgrade --no-cache

RUN apk add --no-cache \
    bash \
    util-linux

RUN python3 -m pip install --no-cache -U discord.py pip

RUN mkdir -m 777 /bot
COPY main.py /bot

COPY init.sh /
RUN chmod +x /init.sh

ENTRYPOINT ["/init.sh"]
