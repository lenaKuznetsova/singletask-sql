#!/bin/bash
. .venv/bin/activate

if [ -f requirements.txt ]; then
  pip install -r requirements.txt
fi

if [ -f docker-compose.yaml ]; then
  docker-compose up
fi