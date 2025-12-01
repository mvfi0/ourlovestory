#!/bin/bash
set -e  # Hentikan script jika ada command yang gagal

echo "Building the project..."
python3.9 -m pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput --clear
echo "Build Completed!"