import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_pd_diplom.settings')
app = Celery('django_pd_diplom')
app.config_from_object('django.conf: settings')
app.autodiscover_tasks()