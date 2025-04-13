"""
WSGI-конфигурация для проекта language_trainer.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "language_trainer.settings")
application = get_wsgi_application()
