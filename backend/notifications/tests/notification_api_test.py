from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from ..models import Notification


class NotificationAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.superuser = User.objects.create_superuser(username='admin', email='admin@example.com', password='admin')
        self.user1 = User.objects.create_user(username='user1', email='user1@example.com', password='user1pass')
        self.user2 = User.objects.create_user(username='user2', email='user2@example.com', password='user2pass')

        # Создание уведомлений
        Notification.objects.create(user=self.user1, notification_type='info', message='Info message 1')
        Notification.objects.create(user=self.user1, notification_type='warning', message='Warning message 1')
        Notification.objects.create(user=self.user2, notification_type='error', message='Error message 1')

    def test_notification_list_superuser(self):
        self.client.force_login(self.superuser)
        response = self.client.get('/api/notifications/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)

    def test_notification_list_regular_user(self):
        self.client.force_login(self.user1)
        response = self.client.get('/api/notifications/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_notification_stats_superuser(self):
        self.client.force_login(self.superuser)
        response = self.client.get('/api/notification-stats/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)

    def test_notification_stats_regular_user(self):
        self.client.force_login(self.user1)
        response = self.client.get('/api/notification-stats/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
