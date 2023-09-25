from django.shortcuts import render
from rest_framework import generics, permissions
from .models import AppUser
from .serializers import UserSerializer

# Create your views here.

class UserList(generics.ListCreateAPIView):
    queryset = AppUser.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateAPIView):
    queryset = AppUser.objects.all()
    serializer_class = UserSerializer

