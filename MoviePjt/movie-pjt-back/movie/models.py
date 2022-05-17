from djongo import models
from accounts.models import User

class Genre(models.Model):
    id = models.IntegerField(unique=True)
    name = models.CharField(max_length=8, unique=True)
        
    class Meta:
        abstract = True

class Movie(models.Model):
    _id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    original_title = models.CharField(max_length=120, null=True, blank=True)
    original_language = models.CharField(max_length=2, null=True, blank=True)
    popularity = models.IntegerField(null=True, blank=True)
    vote_count = models.IntegerField(null=True, blank=True)
    vote_average = models.IntegerField(null=True, blank=True)
    overview = models.TextField(null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    poster_path = models.CharField(max_length=100, null=True, blank=True)
    backdrop_path = models.CharField(max_length=100, null=True, blank=True)
    youtube_path = models.CharField(max_length=100, null=True, blank=True)
    genres = models.ArrayField(model_container=Genre)

    def __str__(self):
        return self.title

class Comment(models.Model):
    _id = models.ObjectIdField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    # last_modified_date = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.content
