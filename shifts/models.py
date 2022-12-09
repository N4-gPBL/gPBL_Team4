from django.db import models
# Create your models here.

class Shift(models.Model):
    shift_id = models.AutoField(primary_key=True)
    shift_date = models.DateField()
    shift_start = models.TimeField(max_length=255)
    shift_end = models.TimeField(max_length=255)
    shift_status = models.BooleanField(default=True)
    shift_created_at = models.DateTimeField(auto_now_add=True)
    shift_updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'shift'

    def __str__(self):
        return self.shift_name

class UserShift(models.Model):
    user_shift_id = models.AutoField(primary_key=True)
    user_shift_user_id = models.ForeignKey('users.User', on_delete=models.CASCADE)
    user_shift_shift_id = models.ForeignKey('shifts.Shift', on_delete=models.CASCADE)
    user_shift_status = models.BooleanField(default=True)
    user_shift_created_at = models.DateTimeField(auto_now_add=True)
    user_shift_updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'user_shift'

    def __str__(self):
        return self.user_shift_user_id