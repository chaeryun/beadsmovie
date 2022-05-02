from djongo import models
from user.models import User

class Genre(models.Model):
    id = models.IntegerField(unique=True)
    name = models.CharField(max_length=8, unique=True)
        
    class Meta:
        abstract = True

class Comment(models.Model):
    _id = models.ObjectIdField()
    user = models.ArrayReferenceField(User, on_delete=models.CASCADE)
    # movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    # last_modified_date = models.DateTimeField(default=created_date)
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.content

class Movie(models.Model):
    _id = models.ObjectIdField()
    title = models.CharField(max_length=52)
    original_title = models.CharField(max_length=52, null=True, blank=True)
    original_language = models.CharField(max_length=2, null=True, blank=True)
    popularity = models.IntegerField(null=True, blank=True)
    vote_count = models.IntegerField(null=True, blank=True)
    vote_average = models.IntegerField(null=True, blank=True)
    overview = models.TextField(null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    poster_path = models.URLField(max_length=100, null=True, blank=True)
    backdrop_path = models.URLField(max_length=100, null=True, blank=True)
    youtube_path = models.URLField(max_length=100, null=True, blank=True)
    genres = models.ArrayField(model_container=Genre)
    comments = models.ArrayReferenceField(Comment, on_delete=models.CASCADE)

    def __str__(self):
        return self.title