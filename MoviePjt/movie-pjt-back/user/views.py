from django.shortcuts import render, redirect, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer


@api_view(["GET"])
def get_user(request):
    User_list = User.objects.all()
    serializer = UserSerializer(User_list, many=True)
    return Response(serializer.data)
