from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    last_login = None
    is_staff = None
    is_superuser = None
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now_add=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    # array images
    images = models.JSONField(default=list)
    shifts = models.ManyToManyField('shifts.Shift', through='shifts.UserShift')
    counter = models.IntegerField(default=0)
    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user'
