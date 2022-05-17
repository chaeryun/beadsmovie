import datetime
from http import HTTPStatus
from django.http import HttpRequest
from django.shortcuts import get_list_or_404, get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi 
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, mixins
from bson import ObjectId
from movie.models import Movie, Comment
from movie.serializers import *
import json
from recommend.reco import get_recommendations, genre_build_chart, vote_count,popularity, vote_average
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
import random
from rest_framework import status


class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = []
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    title = openapi.Parameter('title', openapi.IN_QUERY, description="movie's title", required=False, type=openapi.TYPE_STRING)
    genre_id = openapi.Parameter('genre_id', openapi.IN_QUERY, description="genre's id", required=False, type=openapi.TYPE_INTEGER)

    @swagger_auto_schema(manual_parameters=[title, genre_id])
    def list(self, request, *args, **kwargs):
        movies = self.filter_queryset(self.get_queryset())
        movie_title = request.GET.get('title', '').strip()
        genre_id = request.GET.get('genre_id', '').strip()
        if movie_title:
            movies = movies.filter(title__icontains=movie_title) | movies.filter(original_title__icontains=movie_title)
        if genre_id:
            genre_id = int(genre_id)
            movies = movies.filter(genres={'id' : genre_id})

        # today = datetime.datetime.today()
        # movies = movies.filter(release_date__lt=datetime.date(today.year, today.month, today.day)).order_by('-release_date')
        movies = movies.order_by('-release_date')
        page = self.paginate_queryset(movies)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(movies, many=True)
        return Response(serializer.data, HTTPStatus.OK)
        

class CommentViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

# TODO: 중복되는 영화/코멘트 값 검증코드를 함수로 빼긴 했는데 잘 작성한 건지 좀 더 고민해보기
# 1. 튜플에 담긴 타입이 일관되지 않음 - 값이 유효한지에 따라 달라지는 반환값이니 깊은 로직이 담긴 게 아니라서 큰 혼동 없을 거 같긴 한데.. 프레임워크나 파이썬 내장함수도 이런 거 봤고
# 2. 익셉션을 던지지 않고 조건문으로만 처리 - 익셉션이 그냥 보기 싫고 성능상의 문제도 있다하고 단순 값 판단이라 스택 트레이싱이 필요 없지만 처리할 예외상황이 한 눈에 안들어오고 인덴트 보기 싫음
    def validate_movie_id(self, movie_id):
        movie = Movie.objects.filter(_id=movie_id)
        if not movie.exists():
            return False, Response('해당하는 영화가 없습니다. movie_id를 다시 확인하세요.', HTTPStatus.NOT_FOUND)

        return True, movie.first()

    def validate_comment_id(self, comment_id, user_id):
        if ObjectId.is_valid(comment_id):
            comment = Comment.objects.filter(_id=ObjectId(comment_id))
            if comment.exists():
                comment = comment.first()
                if user_id is not comment.user_id:
                    return False, Response(HTTPStatus.FORBIDDEN)

                return True, comment

        return False, Response('해당하는 코멘트가 없습니다. comment_id를 다시 확인하세요.', HTTPStatus.NOT_FOUND)

    def create(self, request, *args, **kwargs):
        movie_id = self.kwargs['movie_id']
        is_valid, result = self.validate_movie_id(movie_id)
        if not is_valid:
            return result
        movie = result

        serializer = CommentSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, HTTPStatus.BAD_REQUEST)
        
        serializer.save(user=request.user, movie=movie)
        return Response(serializer.data, HTTPStatus.CREATED)

    def list(self, request, *args, **kwargs):
        is_valid, result = self.validate_movie_id(self.kwargs['movie_id'])
        if not is_valid:
            return result
        movie = result
        comments = Comment.objects.filter(movie=movie)

        page = self.paginate_queryset(comments)
        if page is not None:
            serializer = CommentSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, HTTPStatus.OK)

        comment = Comment.objects.get(_id=ObjectId(comment_id))
        comment_writer_id = Comment.objects.get(_id=ObjectId(comment_id)).user_id
        if request.user.id is not comment_writer_id:
            return Response(HTTPStatus.FORBIDDEN)

    def update(self, request, *args, **kwargs):
        is_valid, result = self.validate_movie_id(self.kwargs['movie_id'])
        if not is_valid:
            return result

        is_valid, result = self.validate_comment_id(self.kwargs['pk'], request.user.id)
        if not is_valid:
            return result
        comment = result

        serializer = CommentSerializer(comment, data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, HTTPStatus.BAD_REQUEST)
        
        serializer.save()
        return Response(serializer.data, HTTPStatus.OK)


    def destroy(self, request, *args, **kwargs):
        is_valid, result = self.validate_movie_id(self.kwargs['movie_id'])
        if not is_valid:
            return result

        is_valid, result = self.validate_comment_id(self.kwargs['pk'], request.user.id)
        if not is_valid:
            return result
        comment = result

        comment.delete()
        return Response(HTTPStatus.NO_CONTENT)

@api_view(["GET"])
@permission_classes([AllowAny])
# @action(methods=['get'], detail=False, permission_classes=[], url_path=r'genre/(?P<genre_id>\w+)')
def reco_detail_movie(request, movie_id):
    movie_list = get_recommendations(movie_id)  #[12,13,14]
    movies = Movie.objects.filter(_id__in=random.sample(movie_list, 3))
    movieserializers = MovieSerializer(movies, many=True)
    return Response(movieserializers.data, status=status.HTTP_202_ACCEPTED)



@api_view(["GET"])
@permission_classes([AllowAny])
def reco_genres_movie(request, genres_id):
    movie_list = genre_build_chart(genres_id)  #[12,13,14]
    movies = Movie.objects.filter(_id__in=random.sample(movie_list, 10))
    movieserializers = MovieSerializer(movies, many=True)
    return Response(movieserializers.data, status=status.HTTP_202_ACCEPTED)
