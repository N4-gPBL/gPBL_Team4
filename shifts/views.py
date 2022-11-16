from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createShift(request):
    pass

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getShift(request, shift_id):
    pass

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAllShifts(request):
    pass

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateShift(request, shift_id):
    pass

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteShift(request, shift_id):
    pass

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def assignShift(request, shift_id):
    pass

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unassignShift(request, shift_id):
    pass