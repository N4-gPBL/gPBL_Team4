from rest_framework import serializers
from .models import User


class UserSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    password = serializers.CharField()
    email = serializers.CharField()
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    is_active = serializers.BooleanField(default=True)
    is_admin = serializers.BooleanField(default=False)
    is_staff = serializers.BooleanField(default=False)
    is_superuser = serializers.BooleanField(default=False)

    def __init__(self, instance=None, data=..., **kwargs):
        super().__init__(instance, data, **kwargs)
        self.fields['id'].read_only = True
        self.fields['password'].required = True
        self.fields['email'].required = True
        self.fields['username'].required = True
        self.fields['first_name'].required = False
        self.fields['last_name'].required = False
        self.fields['is_active'].required = False
        self.fields['is_admin'].required = False
        self.fields['is_staff'].required = False
        self.fields['is_superuser'].required = False
        self.fields['last_login'].required = False
        self.fields['date_joined'].required = False
    
    class Meta:
        model = User
        fields = ('id', 'password', 'email', 'username', 'first_name', 'last_name', 'is_active', 'is_admin', 'is_staff', 'is_superuser', 'last_login', 'date_joined')
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)