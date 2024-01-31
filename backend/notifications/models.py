from django.db import models
from django.contrib.auth.models import User

from .choices import NotificationType
from .bases import DateTimeBaseModel


class Notification(DateTimeBaseModel):
    """
    Модель для хранения уведомлений, унаследованная от класса DateTimeBaseModel

    Содержит информацию о пользователе, типе уведомления и сообщении.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    notification_type = models.CharField(max_length=32, choices=NotificationType, verbose_name='Тип уведомления')
    message = models.TextField(verbose_name='Сообщение')

    class Meta:
        verbose_name = 'Уведомление'
        verbose_name_plural = 'Уведомления'

    def __str__(self):
        return 'Уведомление №%s пользователя %s (тип %s)' % (self.pk, self.user, self.notification_type)
