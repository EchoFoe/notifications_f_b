# Generated by Django 5.0.1 on 2024-01-31 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0003_alter_notification_notification_type'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Statistics',
        ),
    ]
