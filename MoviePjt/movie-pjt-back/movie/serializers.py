from rest_framework import serializers
from movie.models import Movie, Comment


class MovieSerializer(serializers.ModelSerializer):

    genres = serializers.JSONField()

    class Meta:
        model = Movie
        fields = ('_id', 'title', 'original_title', 'overview', 'release_date',
        'poster_path', 'backdrop_path', 'youtube_path', 'genres')

    def to_internal_value(self, data):
        if data['release_date'] == '':
            data['release_date'] = None
        return super(MovieSerializer, self).to_internal_value(data)


class CommentSerializer(serializers.ModelSerializer):

    simple_user = serializers.SerializerMethodField()
    
    class Meta:
        model = Comment
        fields = ('_id', 'simple_user', 'created_date', 'content')
        read_only_fields = ('_id', 'simple_user', 'created_date',)

    def get_simple_user(self, obj):
        simple_user = {
            'user_id': obj.user.id,
            'user_nickname': obj.user.nickname,
        }

        return simple_user
            
