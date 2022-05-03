from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import lists, create, update, delete, detail

urlpatterns = [
    path('lists/', lists),
    path('create/', create),
    path('update/<int:article_pk>/', update),
    path('delete/<int:article_pk>/', delete),
    path('detail/<int:article_pk>/', detail),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)