from django.contrib import admin
from django.utils.html import format_html

from .models import Notification
from .choices import NotificationType


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    """ Админ-панель Уведомлений """

    def get_notification_type_display(self, obj: Notification) -> str:
        """
        Возвращает HTML-код для отображения типа уведомления с определенным цветом.

        Args:
            obj (Notification): Объект уведомления.

        Returns:
            str: HTML-код для отображения типа уведомления с цветом.
        """
        colors = {
            NotificationType.ERROR_TYPE: 'red',
            NotificationType.WARNING_TYPE: 'yellow',
            NotificationType.INFO_TYPE: 'green',
        }
        color = colors.get(obj.notification_type, 'black')
        return format_html('<span style="color:{};">{}</span>', color, obj.get_notification_type_display())

    save_as = True
    fieldsets = (
        ('Основная информация', {'fields': (('user', 'notification_type'),)}),
        ('Дополнительная информация', {'fields': ('message',)}),
        ('Даты', {'fields': (('created_at', 'updated_at'),)}),
    )
    get_notification_type_display.short_description = 'Тип уведомления'

    list_display = ['user', 'get_notification_type_display', 'created_at']
    list_filter = ['notification_type', 'user']
    search_fields = ['user']
    readonly_fields = ['created_at', 'updated_at']
