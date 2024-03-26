#!/bin/sh

set -e

poetry run alembic upgrade head
poetry run -- uvicorn src.main:app --host 0.0.0.0 --port 8118
