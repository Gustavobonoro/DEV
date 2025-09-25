"""
ASGI config for geraldi project.
"""
import os
from django.core.asgi import get_asgi_application

# CORREÇÃO: Altere 'geraldi.settings' para 'core.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_asgi_application()