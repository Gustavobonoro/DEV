#!/usr/bin/env bash
# sai em caso de erro
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate