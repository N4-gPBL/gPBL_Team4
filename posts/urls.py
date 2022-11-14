from django.urls import path, include
from . import views
urlpatterns = [
    path('create', views.createPost, name='createPost'),
    path('get/<int:post_id>', views.getPost, name='getPost'),
    path('list', views.getAllPosts, name='getAllPosts'),
    path('update/<int:post_id>', views.updatePost, name='updatePost')
]