#!/usr/bin/env bash
# exit on error

set -o errexit

python manage.py migrate
pip install --upgrade pip
pip install -r requirements.txt
python manage.py collectstatic --no-input