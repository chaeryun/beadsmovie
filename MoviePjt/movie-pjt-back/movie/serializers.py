from rest_framework import serializers
from bson import ObjectId
from movie.models import Movie, Comment
from user.models import User
from user.serializers import UserSerializer


class MovieSerializer(serializers.ModelSerializer):

    genres = serializers.JSONField()

    class Meta:
        model = Movie
        fields = ('_id', 'title', 'original_title', 'overview', 'release_date',
        'poster_path', 'backdrop_path', 'youtube_path', 'genres')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('_id', 'user', 'created_date', 'content')
        read_only_fields = ['_id', 'user']
