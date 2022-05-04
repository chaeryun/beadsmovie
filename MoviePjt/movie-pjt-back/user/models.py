from djongo import models


class User(models.Model):
    _id = models.ObjectIdField()
    kakao_id = models.BigIntegerField(unique=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=8, null=True, blank=True)
    register_date = models.DateField(auto_now_add=True)
    is_valid = models.BooleanField(default=True)
    unregister_date = models.DateField(default=None)
    refresh_token = models.CharField(max_length=64)
