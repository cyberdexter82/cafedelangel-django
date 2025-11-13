#!/bin/bash

echo "Ejecutando collectstatic..."
python manage.py collectstatic --noinput --clear

echo "Iniciando Gunicorn..."
gunicorn backend.wsgi:application --bind=0.0.0.0 --timeout 600