from functools import partial
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from super_types.models import SuperType
from .models import Power, Super
from .serializers import SuperSerializer, PowerSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def supers_list(request):
    if request.method == 'GET':
        type_param = request.query_params.get('type')
        if type_param:
            supers = Super.objects.all()
            supers = supers.filter(super_type__type=type_param)
            serializer = SuperSerializer(supers, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            super_types = SuperType.objects.all()
            custom_response_dictionary = {}
            for super_type in super_types:
                supers = Super.objects.filter(super_type_id=super_type.id)
                super_serializer = SuperSerializer(supers, many=True)
                custom_response_dictionary[super_type.type] = {
                    "Supers": super_serializer.data,
                }
            return Response(custom_response_dictionary, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def super_details(request, pk):
    single_super = get_object_or_404(Super, pk=pk)
    if request.method == 'GET':
        serializer = SuperSerializer(single_super)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = SuperSerializer(single_super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PATCH':
        power_param = request.query_params.get('powers')
        if power_param:
            power = Power.objects.filter(name=power_param)
            if power.exists():
                power = power.get(name=power_param)
            else:
                power = Power(name=power_param)
                power.save()
            single_super.powers.add(power)
            single_super.save()
            serializer = SuperSerializer(single_super)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_404_BAD_REQUEST)
    elif request.method == 'DELETE':
        single_super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
