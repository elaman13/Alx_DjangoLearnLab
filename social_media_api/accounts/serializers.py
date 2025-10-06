from rest_framework import serializers
from . import models
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.validators import ValidationError

custom_user = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = custom_user
        fields = ['username', 'email', 'password']
    
    def create(self, validated_data):
        user = custom_user.objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)
    
    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            token, _ = Token.objects.get_or_create(user=user)
            return {'username': user.username, 'token': token.key}
        return ValidationError('Invalid Informations.')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = custom_user
        fields = ['username', 'email', 'bio', 'profile_picture']