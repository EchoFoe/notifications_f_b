from django.db import models


class NotificationType(models.TextChoices):
    INFO_TYPE = 'info', 'Информационное'
    WARNING_TYPE = 'warning', 'Предупреждающее'
    ERROR_TYPE = 'error', 'С ошибкой'
