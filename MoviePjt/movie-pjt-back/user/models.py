from pyexpat import model
from django.db import models


class User(models.Model):
    id = models.BigIntegerField(primary_key=True)
    email = models.EmailField(unique=True)
    register_date = models.DateField(auto_now=True)
    token = models.CharField(max_length=64)
