from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Super
from .serializers import SuperSerializer

# Create your views here.

@api_view(['GET'])
def supers_list(request):
    if request.method == 'GET':
        supers = Super.objects.all()
        serializer = SuperSerializer(supers, many=True)
        return Response(serializer.data)



@api_view(['GET'])
def super_details(request, pk):
    if request.method == 'GET':
        single_super = get_object_or_404(Super, pk=pk)
        serializer = SuperSerializer(single_super)
        return Response(serializer.data)