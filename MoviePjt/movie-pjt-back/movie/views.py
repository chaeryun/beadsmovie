from http import HTTPStatus
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, mixins
from bson import ObjectId
from movie.models import Movie, Comment
from movie.serializers import *
from accounts.models import User


class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = []
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    @action(methods=['get'], detail=False, permission_classes=[], url_path=r'genre/(?P<genre_id>\w+)')
    def list_by_genre(self, request, *args, **kwargs):
        genre_id = int(self.kwargs['genre_id'])
        movies = Movie.objects.filter(genres={'id' : genre_id})

        page = self.paginate_queryset(movies)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(movies, many=True)
        return Response(serializer.data)


class CommentViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        movie_id = self.kwargs['movie_id']
        movie = Movie.objects.filter(_id=movie_id)
        if not movie.exists():
            return Response('해당하는 영화가 없습니다. movie_id를 다시 확인하세요.', HTTPStatus.NOT_FOUND)

        content = request.data['content']
        comment = Comment(content=content)
        comment.user.add(request.user)
        comment.movie.add(movie.first())
        comment.save()
        
        serializer = CommentSerializer(comment)
        return Response(serializer.data, HTTPStatus.CREATED)
        
    def list(self, request, *args, **kwargs):
        movie_id = self.kwargs['movie_id']
        movie = Movie.objects.filter(_id=movie_id)
        if not movie.exists():
            return Response('해당하는 영화가 없습니다. movie_id를 다시 확인하세요.', HTTPStatus.NOT_FOUND)

        movie = movie.first()
        comments = Comment.objects.filter(movie=movie)

        page = self.paginate_queryset(comments)
        if page is not None:
            serializer = CommentSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


    def update(self, request, *args, **kwargs):
        movie_id = self.kwargs['movie_id']
        movie = Movie.objects.filter(_id=movie_id)
        if not movie.exists():
            return Response('해당하는 영화가 없습니다. movie_id를 다시 확인하세요.', HTTPStatus.NOT_FOUND)
        
        comment_id = self.kwargs['pk']
        comment = Comment.objects.filter(_id=ObjectId(comment_id))
        if not comment.exists():
            return Response('해당하는 리뷰가 없습니다. comment_id를 다시 확인하세요.', HTTPStatus.NOT_FOUND)
            
        comment_writer_id = comment.first().user_id.pop()
        if request.user.id is not comment_writer_id:
            Response(HTTPStatus.FORBIDDEN)
        comment.update(content=request.data['content'])

        serializer = CommentSerializer(comment.first())
        return Response(serializer.data)


    def destroy(self, request, *args, **kwargs):
        movie_id = self.kwargs['movie_id']
        movie = Movie.objects.filter(_id=movie_id)
        if not movie.exists():
            return Response('해당하는 영화가 없습니다. movie_id를 다시 확인하세요.', HTTPStatus.NOT_FOUND)

        comment_id = self.kwargs['pk']
        if not ObjectId.is_valid(comment_id) or not Comment.objects.filter(_id=ObjectId(comment_id)).exists():
            return Response('해당하는 리뷰가 없습니다. comment_id를 다시 확인하세요.', HTTPStatus.NOT_FOUND)

        comment = Comment.objects.get(_id=ObjectId(comment_id))
        comment_writer_id = Comment.objects.get(_id=ObjectId(comment_id)).user_id.pop()
        if request.user.id is not comment_writer_id:
            Response(HTTPStatus.FORBIDDEN)

        comment.delete()
        return Response(HTTPStatus.NO_CONTENT)

