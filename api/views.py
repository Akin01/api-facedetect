from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import tempData
from .serializers import tempSerializer

@api_view(['GET'])
def allTemp(request):
    qs = tempData.objects.all()
    serializer = tempSerializer(qs, many=True)

    if request.method == 'GET':
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def insertTemp(request):

    if request.method == 'POST':
        serializer = tempSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REUQEST)
