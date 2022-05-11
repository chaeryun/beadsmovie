from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    SEX_CHOICES = {
        ('male', 'Male'),
        ('female', 'Female'),
    }

    OCCUPATION_CHOICE = {
        ('student', 'Student'),
        ('professor', 'Professor'),
        ('consultant', 'Consultant'),
        ('manager', 'Manager'),
        ('other', 'Other'),
    }

    nickname = models.CharField(max_length=50)
    age = models.CharField(max_length=20)
    sex = models.CharField(max_length=10, choices=SEX_CHOICES, null=False, default="male")
    occupation = models.CharField(max_length=50, choices=OCCUPATION_CHOICE, null=False, default="student")

    followers = models.ManyToManyField('self', symmetrical=False, related_name='followings')