from .models import Shift,UserShift

class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = ('id','shift_start', 'shift_end','shift_date', 'shift_status', 'shift_created_at', 'shift_updated_at')
    
    def __init__(self, instance=None, data=..., **kwargs):
        super().__init__(instance, data, **kwargs)
        self.fields['id'].read_only = True
        self.fields['shift_start'].required = True
        self.fields['shift_end'].required = True
        self.fields['shift_date'].required = True
        self.fields['shift_status'].required = False
        self.fields['shift_created_at'].required = False
        self.fields['shift_updated_at'].required = False



class UserShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserShift
        fields = ('id', 'user_shift_user_id', 'user_shift_shift_id', 'user_shift_status', 'user_shift_created_at', 'user_shift_updated_at')
    
    def __init__(self, instance=None, data=..., **kwargs):
        super().__init__(instance, data, **kwargs)
    
    def create(self, validated_data):
        user_shift = UserShift.objects.create(**validated_data)
        return user_shift
    