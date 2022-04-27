from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('oauth/kakao/', views.redirect_kakao_permission_code),
    path('oauth/kakao/callback', views.kakao_login),
    path('oauth/kakao/logout', views.kakao_logout),
]
