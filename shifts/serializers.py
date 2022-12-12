from .models import Shift,UserShift
from rest_framework import serializers
class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = ('shift_id','shift_start', 'shift_end','shift_date', 'shift_status', 'shift_created_at', 'shift_updated_at','users')
    
    def __init__(self, instance=None, data=..., **kwargs):
        super().__init__(instance, data, **kwargs)
        self.fields['shift_id'].read_only = True
        self.fields['shift_start'].required = True
        self.fields['shift_end'].required = True
        self.fields['shift_date'].required = True
        self.fields['shift_status'].required = False
        self.fields['shift_created_at'].required = False
        self.fields['shift_updated_at'].required = False
        self.fields['users'].required = False
    def create(self, validated_data):
        shift = Shift.objects.create(**validated_data)
        return shift
    def update(self, instance, validated_data):
        instance.shift_start = validated_data.get('shift_start', instance.shift_start)
        instance.shift_end = validated_data.get('shift_end', instance.shift_end)
        instance.shift_date = validated_data.get('shift_date', instance.shift_date)
        instance.shift_status = validated_data.get('shift_status', instance.shift_status)
        instance.shift_created_at = validated_data.get('shift_created_at', instance.shift_created_at)
        instance.shift_updated_at = validated_data.get('shift_updated_at', instance.shift_updated_at)
        instance.save()
        return instance


class UserShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserShift
        fields = ('user_shift_user_id', 'user_shift_shift_id', 'user_shift_status', 'user_shift_created_at', 'user_shift_updated_at')
    
    def __init__(self, instance=None, data=..., **kwargs):
        super().__init__(instance, data, **kwargs)
    
    def create(self, validated_data):
        user_shift = UserShift.objects.create(**validated_data)
        return user_shift

    
class UsersShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserShift
        fields = ('user_shift_user_id', 'user_shift_shift_id', 'user_shift_status', 'user_shift_created_at', 'user_shift_updated_at','user')
    
    def __init__(self, instance=None, data=..., **kwargs):
        super().__init__(instance, data, **kwargs)