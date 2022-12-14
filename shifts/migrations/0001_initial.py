# Generated by Django 4.1.3 on 2022-11-16 08:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('shift_id', models.AutoField(primary_key=True, serialize=False)),
                ('shift_date', models.DateField()),
                ('shift_start', models.TimeField(max_length=255)),
                ('shift_end', models.TimeField(max_length=255)),
                ('shift_status', models.BooleanField(default=True)),
                ('shift_created_at', models.DateTimeField(auto_now_add=True)),
                ('shift_updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'shift',
            },
        ),
        migrations.CreateModel(
            name='UserShift',
            fields=[
                ('user_shift_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_shift_status', models.BooleanField(default=True)),
                ('user_shift_created_at', models.DateTimeField(auto_now_add=True)),
                ('user_shift_updated_at', models.DateTimeField(auto_now=True)),
                ('user_shift_shift_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shifts.shift')),
                ('user_shift_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_shift',
            },
        ),
    ]
