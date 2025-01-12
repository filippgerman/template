#!/bin/sh
set -e

echo "Running Alembic migrations"
alembic upgrade head
echo "Alembic upgrade head"

uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
