from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from articles.models import Article
from articles.serializers import ArticleListSerializer


@api_view(['GET'])
def lists(request):
    articles = Article.objects.all()
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create(request):
    serializer = ArticleListSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
def update(request, article_pk):
    articles = get_object_or_404(Article, pk=article_pk)

    if not request.user.articles.filter(pk=article_pk).exists():
        return Response({'message': '권한이 없습니다.'})

    serializer = ArticleListSerializer(articles, data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data)


@api_view(['DELETE'])
def delete(request, article_pk):
    articles = get_object_or_404(Article, pk=article_pk)

    if not request.user.articles.filter(pk=article_pk).exists():
        return Response({'message': '권한이 없습니다.'})

    articles.delete()
    return Response({'id': article_pk})


@api_view(['GET'])
def detail(request, article_pk):
    articles = get_object_or_404(Article, pk=article_pk)
    serializer = ArticleListSerializer(articles)
    return Response(serializer.data)



