#!/bin/sh

# Exit immediately if a command exits with a non-zero status
set -e

python3 manage.py makemigrations
python3 manage.py migrate
gunicorn --bind 0.0.0.0:8000 littlelemon.wsgi:application