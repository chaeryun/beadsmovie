from django.contrib import admin

# Register your models here.
from .models import MovieList

admin.site.register(MovieList)