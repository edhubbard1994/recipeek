FROM python:3.7-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /app

COPY requirements.txt /app

WORKDIR /app
RUN pip install -r requirements.txt

COPY . /app

ENV EDAMAM_API_KEY="NONE"
ENV EDAMAM_APP_ID="NONE"

ENTRYPOINT [ "python" ]
CMD [ "scheduler.py" ]


