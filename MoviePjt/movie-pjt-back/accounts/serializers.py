from rest_framework import serializers
from django.contrib.auth import get_user_model

from accounts.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'nickname', 'password', 'email', 'age', 'sex', 'occupation', 'date_joined',
                  'followings', 'followers', 'like_articles')
        read_only_fields = ('followings', 'followers', 'like_articles')