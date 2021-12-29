FROM python:3.8.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
#psycopg
RUN apk update \ 
    && apk add postgresql-dev gcc python3-dev musl-dev 

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

#Рабочая dir
ENV HOME=/home/movies_admin/
ENV APP_HOME=/home/movies_admin/

WORKDIR $APP_HOME

COPY . .
