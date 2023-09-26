from rest_framework import serializers
from .models import AppUser

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = AppUser
        fields = ['id', 'username', 'user_type']

class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = AppUser
        fields = ['username', 'email', 'user_type', 'password']
