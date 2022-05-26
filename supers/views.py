from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Super

# Create your views here.

@api_view(['GET'])
def supers_list(request):
    pass


@api_view(['GET'])
def super_details(request):
    pass