from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from celery_test.celery import create_users_async


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()

    @action(detail=False, methods=['POST'])
    def create_users(self, request, *args, **kwargs):
        is_async = request.data['is_async']
        user_count = request.data['user_count']

        if is_async:
            create_users_async.delay(user_count)
        else:
            create_users_async(user_count)

        return Response(data={'user_count': user_count}, status=status.HTTP_201_CREATED)
