#!/bin/sh

python3 manage.py migrate

/usr/local/bin/gunicorn -w 3 task_manager.wsgi -b 0.0.0.0:$PORT

exec "$@"
