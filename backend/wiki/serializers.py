from dataclasses import fields
from itertools import product
from statistics import mode
from tkinter.tix import Tree
from turtle import title
from xmlrpc.client import Boolean
from rest_framework import serializers
from wiki.models import Page, Type

class page_serializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ['pk', 'name', 'type', 'content']

class Type_serializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['pk', 'name', 'icon_name']



class ocr_serializer(serializers.Serializer):
    json = serializers.JSONField()
    image = serializers.CharField()
