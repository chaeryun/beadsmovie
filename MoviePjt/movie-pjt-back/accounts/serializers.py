from rest_framework import serializers
from django.contrib.auth import get_user_model

from accounts.models import Profile

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'age', 'sex', 'occupation', 'date_joined')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('image', 'nickname', 'message')