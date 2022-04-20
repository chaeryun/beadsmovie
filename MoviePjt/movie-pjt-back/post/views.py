from django.shortcuts import render, redirect, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer


@api_view(["GET"])
def get_post(request):
    Post_list = Post.objects.all()
    serializer = PostSerializer(Post_list, many=True)
    return Response(serializer.data)
