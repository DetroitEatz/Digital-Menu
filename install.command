#!/bin/bash
pip install -r requirements/local.txt
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser
