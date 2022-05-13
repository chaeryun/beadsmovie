from rest_framework import serializers

from articles.models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):
    userName = serializers.SerializerMethodField()

    def get_userName(self, obj):
        return obj.user.username

    class Meta:
        model = Article
        fields = ('id', 'userName', 'user', 'title', 'content', 'image', 'created_at', 'updated_at', 'like_users')
        read_only_fields = ('user', 'like_users')


class CommentSerializer(serializers.ModelSerializer):
    userName = serializers.SerializerMethodField()

    def get_userName(self, obj):
        return obj.user.username

    class Meta:
        model = Comment
        fields = ('id', 'userName', 'user', 'content', 'created_at', 'updated_at', 'article')
        read_only_fields = ('user', 'article')