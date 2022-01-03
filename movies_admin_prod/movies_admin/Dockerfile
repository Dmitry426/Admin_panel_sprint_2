FROM python:3.9.6-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

#Рабочая dir
ENV HOME=/home/movies_admin/
ENV APP_HOME=/home/movies_admin/
WORKDIR $APP_HOME

COPY . .

CMD ["gunicorn"  , "--bind", "0.0.0.0:8000", "config.wsgi:application"]