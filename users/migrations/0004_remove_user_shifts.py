# Generated by Django 4.1.4 on 2022-12-12 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_images_user_shifts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='shifts',
        ),
    ]
