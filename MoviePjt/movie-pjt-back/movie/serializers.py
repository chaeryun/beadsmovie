from rest_framework import serializers
from .models import Movie, Comment
from user.models import User


class MovieSerializer(serializers.ModelSerializer):

    _id = serializers.CharField()
    genres = serializers.JSONField()

    class Meta:
        model = Movie
        fields = ('_id', 'title', 'original_title', 'overview', 'release_date',
        'poster_path', 'backdrop_path', 'youtube_path', 'genres')


# class MovieListSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Movie
#         fields = ('_id', 'title', 'poster_path',)


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('_id', 'user', 'created_date', 'content')
        read_only_fields = ['_id', 'user']


# class CommentListSerializer(serializers.ModelSerializer):

#     user_nickname = User.nickname
#     class Meta:
#         model = Comment
#         fields = ('id', 'user_nickname', 'last_modified_date', 'content')
