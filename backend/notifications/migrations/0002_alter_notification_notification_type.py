# Generated by Django 5.0.1 on 2024-01-31 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notification_type',
            field=models.CharField(choices=[(1, 'Информационное'), (2, 'Предупреждающее'), (3, 'С ошибкой')], max_length=1, verbose_name='Тип уведомления'),
        ),
    ]
