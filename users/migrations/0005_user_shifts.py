# Generated by Django 4.1.4 on 2022-12-12 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shifts', '0002_shift_users'),
        ('users', '0004_remove_user_shifts'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='shifts',
            field=models.ManyToManyField(through='shifts.UserShift', to='shifts.shift'),
        ),
    ]
