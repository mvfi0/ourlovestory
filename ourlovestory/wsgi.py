import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ourlovestory.settings')

application = get_wsgi_application()

# Tambahkan baris ini agar Vercel bisa menemukan aplikasinya
app = application