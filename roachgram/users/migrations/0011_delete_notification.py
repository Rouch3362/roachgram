# Generated by Django 5.0.2 on 2024-05-03 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_rename_notifications_notification'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Notification',
        ),
    ]
