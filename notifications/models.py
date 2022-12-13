from django.db import models
from users.models import User
# Create your models here.

class Notifications(models.Model):
    id = models.AutoField(primary_key=True)
    notifications_user_id = models.ForeignKey('users.User', on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    time = models.DateTimeField()
    status = models.IntegerField()
    user = []
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message

    class Meta:
        db_table = 'notifications'