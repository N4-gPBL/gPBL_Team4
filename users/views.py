from django.shortcuts import render

# Create your views here.


import datetime
from .models import User
from shifts.models import *
from rest_framework import serializers
from .serializers import UserSerializers
from shifts.serializers import ShiftSerializer, UserShiftSerializer,UsersShiftSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.core.files.storage import FileSystemStorage

@api_view(['POST'])
def UserRegisterView(request):
    serializer = UserSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Get list users
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAllUsers(request):
    isActive = request.query_params.get('isActive')
    if isActive is None:
        users = User.objects.all()
    else:
        users = User.objects.all().filter(is_active=isActive)

    serializer = UserSerializers(users, many=True)
 
    for data in serializer.data:
        if len(data['shifts']) > 0:
            shifts = data['shifts']
            data['shifts'] = []
            for shift in shifts:
                shift_detail = Shift.objects.filter(shift_id=shift)
                data['shifts'].append(ShiftSerializer(shift_detail, many=True).data[0])
    return Response(serializer.data, status=status.HTTP_200_OK)

#Get today's shift of user
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserById(request, user_id):
    user = User.objects.filter(id=user_id).prefetch_related('shifts')
    serializer = UserSerializers(user, many=True)
    # get shift detail
    if len(serializer.data) == 0:
        return Response('User not found', status=status.HTTP_404_NOT_FOUND)
    else:
        data = serializer.data[0]
        shifts = data['shifts']
        data['shifts'] = []
        for shift in shifts:
            shift_detail = Shift.objects.filter(shift_id=shift)
            data['shifts'].append(ShiftSerializer(shift_detail, many=True).data[0])
        return Response(serializer.data[0], status=status.HTTP_200_OK)

#Upload images
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def uploadImages(request, user_id):
    user = User.objects.get(id=user_id)
    #Generate image name
    image_name = user.username + '_' + str(datetime.datetime.now().timestamp()) + '.jpg'
    #Get image from form
    image = request.FILES['image']
    #Save image to folder
    fs = FileSystemStorage()
    fs.save(image_name, image)
    #Save image name to user images field
    user.images.append(image_name)
    user.save()
    return Response('Upload image successfully', status=status.HTTP_200_OK)
    
#Delete images
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteImages(request, user_id):
    user = User.objects.get(id=user_id)
    #Get image name from request
    image_name = request.data['image_name']
    #Remove image from folder
    fs = FileSystemStorage()
    fs.delete(image_name)
    #Remove image name from user images field
    user.images.remove(image_name)
    user.save()
    return Response('Delete image successfully', status=status.HTTP_200_OK)