from rest_framework import serializers
from .models import MovieList

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieList
        fields = '__all__'