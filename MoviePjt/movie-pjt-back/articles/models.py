from django.conf import settings
from django.db import models

# Create your models here.
class Article(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="articles")
  title = models.CharField(max_length=100)
  content = models.TextField()
  image = models.ImageField(upload_to='articles/', null=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)