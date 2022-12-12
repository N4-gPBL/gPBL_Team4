from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import ShiftSerializer, UserShiftSerializer,UsersShiftSerializer
from users.serializers import UserSerializers
from rest_framework.response import Response
from rest_framework import status
from .models import Shift,UserShift
import sys
from users.models import User
import datetime
import jwt
from django.conf import settings
# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createShift(request):
    serializer = ShiftSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getShift(request, shift_id):
    print(shift_id)
    shift = Shift.objects.filter(shift_id=shift_id)
    serializer = ShiftSerializer(shift, many=True)
    if len(serializer.data) == 0:
        return Response('Shift not found', status=status.HTTP_404_NOT_FOUND)
    else:
        data = serializer.data[0]
        users = data['users']
        data['users'] = []
        for user in users:
            user_detail = User.objects.filter(id=user)
            data['users'].append(UserSerializers(user_detail, many=True).data[0])
    return Response(serializer.data[0], status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAllShifts(request):
    shifts = Shift.objects.all()
    serializer = ShiftSerializer(shifts, many=True)
    for data in serializer.data:
        users = data['users']
        data['users'] = []
        for user in users:
            user_detail = User.objects.filter(id=user)
            data['users'].append(UserSerializers(user_detail, many=True).data[0])
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateShift(request, shift_id):
    shift = Shift.objects.get(shift_id=shift_id)
    serializer = ShiftSerializer(instance=shift, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteShift(request, shift_id):
    shift = Shift.objects.get(shift_id=shift_id)
    shift.delete()
    return Response('Shift successfully deleted!', status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def assignShift(request, shift_id):
    shift = Shift.objects.get(shift_id=shift_id)
  
    token = request.headers['Authorization'].split(' ')[1]
    user_data = jwt.decode(token, settings.SIMPLE_JWT['SIGNING_KEY'], algorithms=["HS256"])
    data = {
        'user_shift_user_id': user_data['user_id'],
        'user_shift_shift_id': shift_id,
        'user_shift_status': True,
    }
    serializer = UserShiftSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unassignShift(request, shift_id):
    shift = Shift.objects.get(shift_id=shift_id)
    user_shift = UserShift.objects.get(user_shift_shift_id=shift)
    user_shift.delete()
    return Response('Unassigned successful', status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUsersInShift(request,shift_id):
    user_shifts = UserShift.objects.filter(user_shift_shift_id=shift_id)
    # user = User.objects.get(user_id=user_shifts.user_shift_user_id)
    
    serializer = UserShiftSerializer(user_shifts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getShiftsOfUser(request):
    token = request.headers['Authorization'].split(' ')[1]
    user_data = jwt.decode(token, settings.SIMPLE_JWT['SIGNING_KEY'], algorithms=["HS256"])
    user_shifts = UserShift.objects.filter(user_shift_user_id=user_data['user_id'])
    serializer = UsersShiftSerializer(user_shifts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

#Get today's shifts
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getShiftsOfUserById(request, user_id):
    users = User.objects.filter(user_id=user_id)
    
    serializer = UserShiftSerializer(user_shifts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)