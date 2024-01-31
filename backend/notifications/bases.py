from django.db import models
from django.utils import timezone


class DateTimeBaseModel(models.Model):
    """
    Абстрактная базовая модель с датой и временем.

    Предоставляет поля для хранения даты создания и даты редактирования для других моделей.
    """

    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    updated_at = models.DateTimeField(default=timezone.now, verbose_name='Дата редактирования')

    def save(self, *args, **kwargs):
        """
        Переопределенный метод сохранения объекта.

        Обновляет поле `updated_at` перед сохранением объекта.
        """
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)

    class Meta:
        abstract = True
