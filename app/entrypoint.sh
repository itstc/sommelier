#!/bin/sh

python manage.py flush --no-input
python manage.py migrate
python manage.py collectstatic --no-input --clear
python manage.py before

exec "$@"
