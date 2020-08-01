from __future__ import absolute_import, unicode_literals

import os
from uuid import uuid4

from celery import Celery, shared_task
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_test.settings')

app = Celery('celery_test', broker='redis://localhost/0')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@shared_task
def create_users_async(user_count):
    User = get_user_model()
    for i in range(user_count):
        User.objects.create(username=f'{uuid4()}')
