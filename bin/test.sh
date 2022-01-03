#!/bin/bash
. .venv/bin/activate
docker-compose -f docker-compose.tests.yaml up
python -m unittest -v
