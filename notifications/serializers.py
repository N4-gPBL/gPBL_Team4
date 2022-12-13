from .models import Notifications
from rest_framework import serializers

class NotificationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notifications
        fields = ('id','notifications_user_id', 'type', 'message', 'time', 'status', 'created_at', 'updated_at','user')
    
    def __init__(self, instance=None, data=..., **kwargs):
        super().__init__(instance, data, **kwargs)
        self.fields['id'].read_only = True
        self.fields['notifications_user_id'].required = True
        self.fields['type'].required = True
        self.fields['message'].required = True
        self.fields['time'].required = True
        self.fields['status'].required = True
        self.fields['created_at'].required = False
        self.fields['updated_at'].required = False
        self.fields['user'].required = False
    def create(self, validated_data):
        notification = Notifications.objects.create(**validated_data)
        return notification