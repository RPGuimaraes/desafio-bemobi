#!/bin/bash

python manage.py makemigrations
python manage.py migrate --no-input
python manage.py test \

exec "$@"