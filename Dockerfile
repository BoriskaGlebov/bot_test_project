FROM python:3.12.0-slim

COPY requirements.txt /app/

RUN pip install -r /app/requirements.txt
#
COPY . /app/

WORKDIR /app

ENTRYPOINT ["python3","main.py"]
