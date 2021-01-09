FROM python:3.7-slim as production

ENV PYTHONUNBUFFERED=1
WORKDIR /app/

RUN apt-get update && \
    apt-get install -y \
    bash \
    build-essentials \
    gcc \
    libffi-dev \
    musl-dev \
    openssl \
    postgresql \
    libpq-dev

COPY requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt

COPY manage.py ./manage.py
COPY website ./website

EXPOSE 8000

FROM production as development

COPY requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt

COPY . .