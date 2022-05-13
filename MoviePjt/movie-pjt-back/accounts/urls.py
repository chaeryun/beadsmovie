from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from .views import signup, delete, profile, my_profile

urlpatterns = [
    path('signup/', signup),
    path('login/', obtain_jwt_token),
    path('delete/<int:user_pk>/', delete),
    path('profile/<int:user_pk>/', profile),
    path('myprofile/', my_profile)
]