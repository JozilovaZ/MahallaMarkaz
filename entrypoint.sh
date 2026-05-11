#!/bin/sh
mkdir -p /app/data
chmod 777 /app/data
python manage.py migrate --noinput
exec gunicorn mahalla_backend.wsgi:application --bind 0.0.0.0:8000 --workers 3
