from django.urls import path
from . import views

urlpatterns = [
    path('create', views.createShift, name='createShift'),
    path('get/<int:shift_id>', views.getShift, name='getShift'),
    path('list', views.getAllShifts, name='getAllShifts'),
    path('update/<int:shift_id>', views.updateShift, name='updateShift'),
    path('delete/<int:shift_id>', views.deleteShift, name='deleteShift'),
    path('assign/<int:shift_id>', views.assignShift, name='assignShift'),
    path('unassign/<int:shift_id>', views.unassignShift, name='unassignShift')
]