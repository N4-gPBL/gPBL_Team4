from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import ShiftSerializer, UserShiftSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Shift,UserShift
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
    shift = Shift.objects.get(shift_id=shift_id)
    serializer = ShiftSerializer(shift, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAllShifts(request):
    shifts = Shift.objects.all()
    serializer = ShiftSerializer(shifts, many=True)
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
    serializer = UserShiftSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unassignShift(request, shift_id):
    shift = Shift.objects.get(shift_id=shift_id)
    user_shift = UserShift.objects.get(user_shift_shift_id=shift)
    user_shift.delete()
    return Response('Item successfully deleted!', status=status.HTTP_200_OK)
