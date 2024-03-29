from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import NotificationsSerializer

from rest_framework.response import Response
from rest_framework import status
from .models import Notifications
from users.models import User
from users.serializers import UserSerializers

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createNotification(request):
    serializer = NotificationsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAllNotifications(request):
    notifications = Notifications.objects.all()

    serializer = NotificationsSerializer(notifications, many=True)
    if len(serializer.data) == 0:
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        notifications_data = serializer.data
        for notification in notifications_data:
            notification['user'] = []
            user_detail = User.objects.filter(id=notification['notifications_user_id'])
            user_serializer = UserSerializers(user_detail, many=True)
            notification['user'].append(user_serializer.data[0])
            notification['user'] = notification['user'][0]

        return Response(notifications_data, status=status.HTTP_200_OK)

