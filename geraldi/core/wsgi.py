"""
WSGI config for geraldi project.
"""
import os
from django.core.wsgi import get_wsgi_application

# CORREÇÃO: Altere 'geraldi.settings' para 'core.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_wsgi_application()