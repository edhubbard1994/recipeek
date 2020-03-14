#!/bin/sh
cd app

echo "-----Making new migrations"
python manage.py makemigrations
#apply migrations
echo "----Apply database migrations"
python manage.py migrate
# Start server
echo "----Starting server"
python manage.py runserver 0.0.0.0:8000