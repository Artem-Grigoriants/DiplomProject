from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer, UserSerializer as BaseUserSerializer
from .models import User

class CustomUserCreateSerializer(BaseUserCreateSerializer):
    """
    Custom serializer for user registration.
    Includes additional fields: is_supplier and is_client.
    """
    class Meta(BaseUserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'password', 'first_name', 'last_name', 'is_supplier', 'is_client')
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True}
        }

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    def validate(self, data):
        if not data.get('is_supplier') and not data.get('is_client'):
            raise serializers.ValidationError("At least one of 'is_supplier' or 'is_client' must be True.")
        return data

class CustomUserSerializer(BaseUserSerializer):
    """
    Custom serializer for user representation.
    Includes additional fields: is_supplier and is_client.
    """
    class Meta(BaseUserSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'is_supplier', 'is_client')