from django.urls import path
from . import views

app_name = 'media'

urlpatterns = [
    path('', views.media),
    path('<int:media_pk>/', views.media_detail),
]
