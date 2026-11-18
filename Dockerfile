FROM python:3.15-alpine

COPY requirements.txt /
RUN pip install -r requirements.txt
COPY webapp.py /

ENTRYPOINT ["python3", "webapp.py"]
