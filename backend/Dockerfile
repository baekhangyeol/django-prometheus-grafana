FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /backend/
WORKDIR /backend

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt