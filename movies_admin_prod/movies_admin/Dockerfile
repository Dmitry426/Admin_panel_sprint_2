FROM python:3.9.6-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

#Рабочая dir
ENV HOME=/home/movies_admin/
ENV APP_HOME=/home/movies_admin/
WORKDIR $APP_HOME
# Заметка ревьюеру:  файл .dockerignore  есть и был изначально но он  стрательоно никак не загружается в ситему яндекс , посмтрите его в гит пожалуйста.
#Building web
#Sending build context to Docker daemon  112.6kB такой размер при сборке
COPY . .

CMD ["gunicorn"  , "--bind", "0.0.0.0:8000", "config.wsgi:application"]
