from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer, UserSerializer as BaseUserSerializer
from .models import User, USER_TYPE_CHOICES

class CustomUserCreateSerializer(BaseUserCreateSerializer):
    """
    Custom serializer for user registration.
    Includes additional fields: company, position, and type.
    """
    class Meta(BaseUserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'password', 'first_name', 'last_name', 'company', 'position', 'type')
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True}
        }

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    def validate(self, data):
        if data.get('type') not in dict(USER_TYPE_CHOICES).keys():
            raise serializers.ValidationError("Invalid user type.")
        return data


class CustomUserSerializer(BaseUserSerializer):
    """
    Custom serializer for representing user data.
    Includes additional fields: company, position, and type.
    """
    class Meta(BaseUserSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'company', 'position', 'type')