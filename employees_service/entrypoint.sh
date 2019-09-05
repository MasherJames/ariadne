#!/bin/sh

# Collect static files
python manage.py collectstatic --noinput
# Remove all data from the database and re-executes any post-synchronization handlers
python manage.py flush --no-input
# Migrate
python manage.py migrate

