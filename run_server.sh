#!/bin/bash
#export FLASK_ENV=development
#python3 ./main.py

gunicorn -w 4 -b 0.0.0.0:5000 --timeout 3600 main:app
