from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.


class MovieList(models.Model):
    _id = models.TextField(auto_created=True, unique=True, primary_key=True)
    title = models.TextField()
    original_title = models.TextField()
    original_lang = models.TextField()
    popularity = models.FloatField(validators=[MinValueValidator(0)])
    vote_count = models.IntegerField(validators=[MinValueValidator(0)])
    vote_average = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    overview = models.TextField()
    release_date = models.TextField()
    poster_path = models.TextField()
    backdrop_path = models.TextField()
    poster_path = models.TextField()
    youtube_path = models.TextField()