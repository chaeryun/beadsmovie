from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from .views import signup, delete, profile

urlpatterns = [
    path('signup/', signup),
    path('login/', obtain_jwt_token),
    path('delete/<int:pk>/', delete),
    path('profile/<int:pk>/', profile)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)