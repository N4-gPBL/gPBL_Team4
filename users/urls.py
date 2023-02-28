from django.urls import path

from . import views

urlpatterns = [
    path('register', views.UserRegisterView, name='register'),
    path('list', views.getAllUsers, name='getAllUsers'),
    path('<int:user_id>', views.getUserById, name='getUserById'),
    path('upload/<int:user_id>', views.uploadImages, name='uploadImages'),
    #Delete images
    path('delete/<int:user_id>', views.deleteImages, name='deleteImages'),
    #Update is active user
    path('update/<int:user_id>', views.updateUser, name='updateUser'),
]