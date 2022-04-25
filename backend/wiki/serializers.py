from dataclasses import fields
from itertools import product
from pyexpat import model
from statistics import mode
from tkinter.tix import Tree
from turtle import title
from xmlrpc.client import Boolean
from rest_framework import serializers
from wiki.models import Page, Type, Attribute


class Type_serializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['pk', 'name', 'icon_name']

class attribute_serializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ['object_name', 'attribute_name', 'attribute_value']

class page_serializer(serializers.ModelSerializer):
    attributes = attribute_serializer(many=True, read_only=True, source='attribute_set')    

    class Meta:
        model = Page
        fields = ['pk', 'name', 'type', 'content', 'attributes']

class ocr_serializer(serializers.Serializer):
    json = serializers.JSONField()
    image = serializers.CharField()
