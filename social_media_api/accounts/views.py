from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from . import models
from . import serializers
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from rest_framework.views import APIView

custom_user = get_user_model()

# Create your views here.
class RegisterView(generics.CreateAPIView):
    serializer_class = serializers.RegisterSerializer
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        data = serializer.data
        data['token'] = token.key
        
        return Response(data, status=status.HTTP_201_CREATED)


class LoginView(generics.CreateAPIView):
    serializer_class = serializers.LoginSerializer
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

class ProfileView(generics.ListAPIView):
    serializer_class = serializers.ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return get_user_model().objects.filter(id=user.id)