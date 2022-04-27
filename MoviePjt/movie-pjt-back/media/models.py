from django.db import models


class Media(models.Model):
    title = models.CharField(max_length=50)
    director = models.CharField(max_length=20)