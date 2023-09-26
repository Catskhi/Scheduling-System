from django.shortcuts import render
from rest_framework import generics, permissions
from .models import AppUser
from .serializers import UserSerializer, CreateUserSerializer

# Create your views here.

class UserList(generics.ListAPIView):
    queryset = AppUser.objects.all()
    serializer_class = UserSerializer

class CreateUser(generics.CreateAPIView):
    serializer_class = CreateUserSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()

class UserDetail(generics.RetrieveUpdateAPIView):
    queryset = AppUser.objects.all()
    serializer_class = UserSerializer

