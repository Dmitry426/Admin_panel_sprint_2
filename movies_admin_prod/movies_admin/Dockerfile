FROM nginx:1.19.2-alpine
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
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
WORKDIR $APP_HOME

#Entrypoint с командами
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g'  $APP_HOME/entrypoint.sh
RUN chmod +x  $APP_HOME/entrypoint.sh


COPY . .

ENTRYPOINT ["sh","/home/movies_admin/entrypoint.sh"]