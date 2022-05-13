from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from accounts.models import User
from articles.models import Article
from articles.serializers import ArticleListSerializer, CommentSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
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
@permission_classes([AllowAny])
def detail(request, article_pk):
    articles = get_object_or_404(Article, pk=article_pk)
    serializer = ArticleListSerializer(articles)
    return Response(serializer.data)


@api_view(['POST'])
def article_like(request, user_pk, article_pk):
    articles = get_object_or_404(Article, pk=article_pk)
    mine = get_object_or_404(User, pk=user_pk)

    if mine.like_articles.filter(pk=articles.pk).exists():
        mine.like_articles.remove(articles.pk)
        likes = False

    else:
        mine.like_articles.add(articles.pk)
        likes = True

    return Response(likes)


@api_view(['GET'])
@permission_classes([AllowAny])
def comment_list(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comments = article.comment_set.all()
    serializer = CommentSerializer(comments, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, article=article)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def comment_update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)

    if not request.user.comments.filter(pk=comment_pk).exists():
        return Response({'message': '권한이 없습니다.'})
    else:
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user, article=article)
        return Response(serializer.data)

@api_view(['DELETE'])
def comment_delete(request, article_pk, comment_pk):
  article = get_object_or_404(Article, pk=article_pk)
  comment = article.comment_set.get(pk=comment_pk)

  if not request.user.comments.filter(pk=comment_pk).exists():
    return Response({'message': '권한이 없습니다.'})
  else:
    comment.delete()
    return Response({ 'id': comment_pk })