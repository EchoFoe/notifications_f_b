from django.urls import path
from .api import NotificationListView, NotificationStatsView, RegisterUserView

urlpatterns = [
    path('notifications/', NotificationListView.as_view(), name='notification_list'),
    path('notification-stats/', NotificationStatsView.as_view(), name='notification_stats'),
    path('register/', RegisterUserView.as_view(), name='register_user'),
]
