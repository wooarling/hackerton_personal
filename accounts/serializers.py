# serializers.py

from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User

# 회원가입용 시리얼라이저
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, max_length=128)

    class Meta:
        model = User
        fields = ['username', 'password', 'name', 'nickname', 'phone', 'gender', 'email', 'birth_date']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

# JWT 로그인용 시리얼라이저
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'username'

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError("No active account found with the given credentials")
        if not user.is_active:
            raise serializers.ValidationError("User is inactive")

        # JWT 토큰 생성
        data = super().validate({'username': username, 'password': password})
        data.update({
            'username': user.username,
            'email': user.email
        })
        return data

