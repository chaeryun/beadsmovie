from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import lists, create, update, delete, detail, article_like, comment_list, comment_create, comment_delete, \
    comment_update

urlpatterns = [
    path('lists/', lists),
    path('create/', create),
    path('update/<int:article_pk>/', update),
    path('delete/<int:article_pk>/', delete),
    path('detail/<int:article_pk>/', detail),

    path('like/<int:user_pk>/<int:article_pk>/', article_like),

    path('comment/list/<int:article_pk>', comment_list),
    path('comment/create/<int:article_pk>/', comment_create),
    path('comment/update/<int:article_pk>/<int:comment_pk>/', comment_update),
    path('comment/delete/<int:article_pk>/<int:comment_pk>/', comment_delete)
]