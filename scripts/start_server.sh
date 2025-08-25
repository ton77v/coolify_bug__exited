#!/bin/bash
# scripts/start_server.sh


# we need to run all the python programs with UV to use the env
uv run gunicorn --worker-class gevent \
  --timeout=60 --log-level debug --capture-output \
  --error-logfile - --access-logfile - \
  --workers 3 --bind 0.0.0.0:5555 -m 007 wsgi:app
