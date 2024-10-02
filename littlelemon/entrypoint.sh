#!/bin/sh

# Exit immediately if a command exits with a non-zero status
set -e

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Start Uvicorn server
echo "Starting Uvicorn..."
exec "$@"