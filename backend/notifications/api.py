from typing import Any, Dict

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

from .serializers import NotificationSerializer, UserSerializer
from .models import Notification
from .choices import NotificationType


class RegisterUserView(APIView):
    """
    Представление для регистрации нового пользователя.

    Принимает POST-запрос с данными нового пользователя в формате JSON.
    Если данные верны, сохраняет нового пользователя и возвращает код состояния 201 CREATED.
    В противном случае, возвращает ошибку и код состояния 400 BAD REQUEST.
    """

    def post(self, request: Any) -> Response:
        """
        Обрабатывает POST-запрос для регистрации нового пользователя.

        Args:
            request (Any): Запрос пользователя с данными нового пользователя.

        Returns:
            Response: Ответ сервера.
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NotificationListView(APIView):
    """
    Представление для получения списка уведомлений.

    Пользователи могут просматривать уведомления в зависимости от своего статуса:
    - Суперпользователи могут видеть все уведомления, распределенные по пользователям.
    - Обычные пользователи видят только свои уведомления.

    Распределение уведомлений по пользователям доступно только суперпользователям.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request: Any) -> Response:
        """
        Получает список уведомлений в зависимости от роли пользователя.

        Если пользователь является суперпользователем, возвращает все уведомления,
        распределенные по пользователям. Иначе, возвращает уведомления только для текущего пользователя.

        Args:
            request (Any): Запрос пользователя.

        Returns:
            Response: Список уведомлений или уведомления пользователя в формате JSON.
        """

        if request.user.is_superuser:
            all_users = User.objects.all()
            user_notifications = {}
            for user in all_users:
                user_notifications[user.username] = Notification.objects.filter(user=user)

            serializer_data = {
                user: NotificationSerializer(notifications, many=True).data
                for user, notifications in user_notifications.items()
            }
            return Response(serializer_data)

        else:
            notifications = Notification.objects.filter(user=request.user)
            serializer = NotificationSerializer(notifications, many=True)
            return Response(serializer.data)


class NotificationStatsView(APIView):
    """
    Представление для получения статистики по уведомлениям.

    Суперпользователи видят статистику по всем пользователям, а обычные пользователи -
    только свою статистику.

    Статистика включает количество уведомлений каждого типа: информационных, предупреждающих и с ошибками.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request: Any) -> Response:
        """
        Получает статистику по уведомлениям в зависимости от роли пользователя.

        Если пользователь является суперпользователем, возвращает статистику по всем пользователям.
        Иначе, возвращает статистику только для текущего пользователя.

        Args:
            request (Any): Запрос пользователя.

        Returns:
            Response: Статистика по уведомлениям в формате JSON.
        """

        if not request.user.is_authenticated:
            return Response({'detail': 'Креды для аутентификации не были предоставлены.'}, status=401)

        stats_data: Dict[str, Dict[str, int]] = {}
        if request.user.is_superuser:

            all_users = User.objects.all()
            for user in all_users:
                notifications = Notification.objects.filter(user=user)
                stats_data[user.username] = self._get_user_statistics(notifications)

        else:
            notifications = Notification.objects.filter(user=request.user)
            stats_data[request.user.username] = self._get_user_statistics(notifications)

        return Response(stats_data)

    def _get_user_statistics(self, notifications) -> Dict[str, int]:
        """
        Вычисляет статистику для пользовательских уведомлений.

        Args:
            notifications: Уведомления пользователя.

        Returns:
            Dict[str, int]: Статистика уведомлений в формате словаря.
        """
        informational_count = notifications.filter(notification_type=NotificationType.INFO_TYPE).count()
        warning_count = notifications.filter(notification_type=NotificationType.WARNING_TYPE).count()
        error_count = notifications.filter(notification_type=NotificationType.ERROR_TYPE).count()

        return {
            'informational_count': informational_count,
            'warning_count': warning_count,
            'error_count': error_count
        }
