from http import HTTPStatus
from django.shortcuts import get_list_or_404, get_object_or_404
# from rest_framework_simplejwt.backends import 
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, mixins
from bson import ObjectId
from movie.models import Movie, Genre, Comment
from movie.serializers import *


class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = []
    permission_classes = []

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def retrieve(self, request, *args, **kwargs):
        self.kwargs["pk"] = ObjectId(self.kwargs["pk"])
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

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
        

    # @action(methods=['get'], detail=False, permission_classes=[], url_path=r'(?P<movie_id>\w+)')
    # def create_review(self, request, *args, **kwargs):
    #     movie_id = ObjectId(self.kwargs['movie_id'])
    #     movie = Movie.objects.filter('_id' == movie_id)

        # review = Comment.objects.create(user= content=request.data)
        # movie.
        # serializer = self.get_serializer(movies, many=True)
        # return Response(serializer.data)
        

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
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    authentication_classes = []
    permission_classes = []

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        self.kwargs["pk"] = ObjectId(self.kwargs["pk"])
        # movie_id = 
        # movie = Movie.objects.filter('_id' = movie_id)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        self.kwargs["pk"] = ObjectId(self.kwargs["pk"])
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    # def update(self, request, *args, **kwargs):
    #     self.kwargs["pk"] = ObjectId(self.kwargs["pk"])
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)

    # def destroy(self, request, *args, **kwargs):
    #     self.kwargs["pk"] = ObjectId(self.kwargs["pk"])
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)
