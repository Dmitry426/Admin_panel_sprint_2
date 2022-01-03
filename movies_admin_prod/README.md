## Django  Movies_admin_panel project for Yandex practicum .

- Project starts in a container and uses docker-compose 
- routing resolved through nginx add gunicorn 

## Minimum Requirements
This project supports Ubuntu Linux 18.04  It is not tested or supported for the Windows OS.

- [Docker 20.10 +](https://docs.docker.com/)
- [docker-compose  1.29.2 + ](https://docs.docker.com/compose/)

# If you already have postgres data volume in your project with matching SQL schemas  
## Quickstart

```bash
$ docker-compose up -d  --bulid 
$ docker-compose exec web python manage.py migrate movies --fake
$ docker-compose exec web python manage.py migrate
$ docker-compose exec web python manage.py collectstatic


```
# If you DO NOT have created postgres data volume in your project with matching SQL schema 
## Create postgres volume
```bash
$ sudo docker run -d --rm \
  --name postgres \
  -p 5432:5432 \
  -v /path/to/movies_admin:/var/lib/postgresql/data \
  -e POSTGRES_PASSWORD=<secret_password> \
  postgres:13 

$ sudo docker exec -it postgres bash 

```
## Inside posgres container run 
```bash
psql -U postgres
CREATE DATABASE <Your database name> ; 
CREATE SCHEMA content;
CREATE SCHEMA django; 

```
##  Start Project 
```bash
$ docker-compose up -d  --bulid 
$ docker-compose exec web python manage.py migrate
$ docker-compose exec web python manage.py migrate movies 
```


# Notes 
- django allowed hosts param should be set through .env file 
- In order to run project docker-compose .env  MUST have DB_HOST="docker-compose database image name" default name is  "postgres"

