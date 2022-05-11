from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('oauth/kakao/', views.kakao_login),
    path('oauth/kakao/logout/', views.kakao_logout),
]
