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


ARG build_mode
RUN if [ "$build_mode" = "migrate" ] ; then python manage.py makemigrations; python manage.py migrate; fi

#RUN python manage.py makemigrations
#RUN python manage.py migrate
EXPOSE 8000

ENTRYPOINT ["python","manage.py"]
CMD [ "runserver","0.0.0.0:8000" ]
