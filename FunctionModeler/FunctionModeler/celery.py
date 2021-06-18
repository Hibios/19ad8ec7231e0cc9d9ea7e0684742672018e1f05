from __future__ import absolute_import, unicode_literals
from django.conf import settings
from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FunctionModeler.settings')
app = Celery('FunctionModeler_tasks', broker=settings.CELERY_BROKER_URL)
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
