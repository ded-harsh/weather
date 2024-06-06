#!/bin/sh
source .venv/bin/activate
python weather_project/manage.py runserver $PORT
