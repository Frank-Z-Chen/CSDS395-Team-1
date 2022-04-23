from http.client import responses
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from wiki.models import Page
from wiki import serializers
# Create your views here.

@api_view(['GET', 'POST'])
def page_list(request, type_name):
    if request.method == 'GET':
        queryset = Page.objects.filter(type__name = type_name).all()
        serializer = serializers.page_serializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = serializers.page_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['GET', 'PUT', 'DELETE'])
def page_detail(request, type_name, page_slug):
    page = get_object_or_404(Page, slug = page_slug)
    if request.method == 'GET':
        serializer = serializers.page_serializer(page)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = serializers.page_serializer(page, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        page.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

