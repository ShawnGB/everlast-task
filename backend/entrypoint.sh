#!/bin/sh
set -e

echo "Waiting for DB..."
until pg_isready -h db -U user -d everlast_db; do
  sleep 1
done

echo "Running migrations..."
alembic upgrade head

echo "Seeding data..."
python seed.py

echo "Starting app..."
exec uvicorn src.app:app --host 0.0.0.0 --port 8000 --reload
