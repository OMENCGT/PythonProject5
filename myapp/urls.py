from django.urls import path, re_path
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path('book', views.book_get_or_post),
    path('author', views.author_post_or_get),
    path('book/<int:pk>', views.book_patch_or_delete),
    path('author/<int:pk>', views.author_patch_or_delete)
]