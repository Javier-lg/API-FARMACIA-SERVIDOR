"""
ASGI config for servidor project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

if os.environ.get('DJANGO_ENV') == 'production':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'servidor.settings.production')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'servidor.settings.local')

application = get_asgi_application()