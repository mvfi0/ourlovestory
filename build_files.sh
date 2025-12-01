#!/bin/bash
set -e  # Hentikan script jika ada command yang gagal

echo "Building the project..."

# 1. Install PIP secara manual karena Vercel kadang tidak menyediakannya di Python 3.9
python3.9 -m ensurepip --default-pip

# 2. Update PIP ke versi terbaru (opsional, tapi disarankan)
python3.9 -m pip install --upgrade pip

# 3. Install dependencies project kamu
python3.9 -m pip install -r requirements.txt

# 4. Jalankan perintah Django
python3.9 manage.py collectstatic --noinput --clear

echo "Build Completed!"