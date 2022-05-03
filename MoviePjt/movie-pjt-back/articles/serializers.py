from rest_framework import serializers

from articles.models import Article


class ArticleListSerializer(serializers.ModelSerializer):
    userName = serializers.SerializerMethodField()

    def get_userName(self, obj):
        return obj.user.username

    class Meta:
        model = Article
        fields = ('id', 'userName', 'user', 'title', 'content', 'image', 'created_at', 'updated_at',)
        read_only_fields = ('user',)