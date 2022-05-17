"""BEADSMOVIE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import routers

from movie.views import MovieViewSet, CommentViewSet
from movie import views


schema_view = get_schema_view(
    openapi.Info(
        title="Beads Movie Swagger",
        default_version='ver 1.0',
        description="Beads Movie에 대한 Swagger입니다.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="이메일"), # 부가정보
        license=openapi.License(name="MIT"),     # 부가정보
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

movie_router = routers.SimpleRouter()
movie_router.register('movie', MovieViewSet)
movie_router.register('movie/(?P<movie_id>[^/.]+)/review', CommentViewSet)

urlpatterns = [
    re_path(r'swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-v1'),
    path('api/admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/articles/', include('articles.urls')),
    path('api/user/', include('user.urls')),
    path('api/', include(movie_router.urls)),
<<<<<<< HEAD
    path('api/movie/<int:movie_id>/', views.reco_detail_movie),
=======
    path('api/similar_movie/<int:movie_id>/', views.reco_detail_movie),
    path('api/similar_movie/genres/<int:genres_id>/', views.reco_genres_movie),
>>>>>>> 2fe33d2e19b875f4b5d87d6b65dbfe5c8fe1c2ac
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

