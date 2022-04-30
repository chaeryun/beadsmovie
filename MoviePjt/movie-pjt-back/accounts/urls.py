from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from .views import signup, delete

urlpatterns = [
    path('signup/', signup),
    path('login/', obtain_jwt_token),
    path('delete/<int:pk>/', delete),
]