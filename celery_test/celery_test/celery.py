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
    print('user_count:', user_count)
    for i in range(user_count):
        User.objects.create(username=f'{uuid4()}')
        print('!!created!!')


@shared_task
def email_async():
    from django.core.mail import EmailMessage
    email = EmailMessage('title', 'content', to=['kjw11077naver@gmail.com'])
    email.send()
    print('email send~')
