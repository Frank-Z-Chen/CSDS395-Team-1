from dataclasses import fields
from itertools import product
from statistics import mode
from turtle import title
from rest_framework import serializers
from wiki.models import Page, Type

class page_serializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ['pk', 'name', 'type', 'content']
