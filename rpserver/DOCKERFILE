FROM python:3.7-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add postgresql-dev 
#    && apk add libressl-dev \
#    && apk add openssl-dev \
#    && apk add tcpdump \
#    && apk add libffi-dev \
#    && apk add libxml2-dev \
#    && apk add libxslt-dev 

COPY docker-entrypoint.sh /

RUN mkdir /app
COPY requirements.txt /app
WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8000

WORKDIR /


ENTRYPOINT ["/docker-entrypoint.sh"]

