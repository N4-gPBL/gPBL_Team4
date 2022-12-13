from django.urls import path
from . import views

urlpatterns = [
    path('create', views.createNotification, name='createNotification'),
    # path('<int:notification_id>', views.getNotification, name='getNotification'),
    path('list', views.getAllNotifications, name='getAllNotifications'),
    # path('update/<int:notification_id>', views.updateNotification, name='updateNotification'),
    # path('delete/<int:notification_id>', views.deleteNotification, name='deleteNotification'),
    # path('user/<int:user_id>', views.getNotificationsOfUser, name='getNotificationsOfUser'),
]