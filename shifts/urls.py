from django.urls import path
from . import views


urlpatterns = [
    path('create', views.createShift, name='createShift'),
    path('<int:shift_id>', views.getShift, name='getShift'),
    path('list', views.getAllShifts, name='getAllShifts'),
    path('update/<int:shift_id>', views.updateShift, name='updateShift'),
    path('delete/<int:shift_id>', views.deleteShift, name='deleteShift'),
    path('assign/<int:shift_id>', views.assignShift, name='assignShift'),
    path('unassign/<int:shift_id>', views.unassignShift, name='unassignShift'),
    path('get_users/<int:shift_id>', views.getUsersInShift, name='getUser'),
    path('users/<int:user_id>', views.getShiftsOfUserById, name='getShifts'),
    path('user_shifts', views.getShiftsOfUser, name='getShifts'),
]