# Сбор статитики и первоначальная настройка
python manage.py migrate
python manage.py migrate movies --fake
python manage.py collectstatic --noinput
gunicorn config.wsgi:application --bind 0.0.0.0:8000
