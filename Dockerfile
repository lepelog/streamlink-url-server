FROM python:3.15-alpine

RUN pip install https://github.com/lepelog/streamlink/archive/refs/heads/twitch-stream-start.zip
COPY webapp.py /

ENTRYPOINT ["python3", "webapp.py"]
