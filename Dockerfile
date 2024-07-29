# syntax=docker/dockerfile:1
FROM python:3.11-slim

# Removes output stream buffering, allowing for more efficient logging
ENV PYTHONUNBUFFERED 1

WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 tripreports.wsgi:application
