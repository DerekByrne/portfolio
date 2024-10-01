FROM python:3.11-slim

WORKDIR /python-mqtt-ingest

RUN python3 -m venv venv
COPY requirements.txt venv/lib/python3.11/site-packages/
RUN venv/bin/pip install -r venv/lib/python3.11/site-packages/requirements.txt

COPY mqtt_config.py .
COPY mqtt-sender.py .

CMD ["venv/bin/python","-u", "mqtt-sender.py"]