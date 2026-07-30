#!/bin/bash
# Post-merge setup for Obusubiri Associates Django project.
# Runs automatically after each task merge.
set -e

echo "→ Installing Python dependencies..."
pip install -r requirements.txt -q

echo "→ Running Django migrations..."
python manage.py migrate --no-input

echo "✓ Post-merge setup complete."
