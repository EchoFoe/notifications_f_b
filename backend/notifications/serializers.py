from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Notification.

    Преобразует объекты Notification в формат JSON и наоборот.
    """

    class Meta:
        model = Notification
        exclude = ['created_at', 'updated_at']


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели User.

    Преобразует объекты User в формат JSON и наоборот.
    """

    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """
        Создает нового пользователя.

        Принимает валидированные данные, создает нового пользователя и возвращает его.
        """
        user = User.objects.create_user(**validated_data)
        return user
