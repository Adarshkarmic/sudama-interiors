"""
ASGI config for sudama project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sudama.settings')

application = get_asgi_application()

if os.environ.get('VERCEL') == '1':
    from django.core.management import call_command
    try:
        call_command('migrate', interactive=False)
    except Exception as e:
        print(f"Error running migrations at startup: {e}")
