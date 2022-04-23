from django.db import models
from . import wiki_util
# Create your models here.

class Type(models.Model):
    ICON_NAME_CHOICE = wiki_util.preprocessed_icon_names()
    name = models.CharField(max_length=255, unique=True)
    model_address = models.CharField(max_length=255, blank=True, null=True)
    icon_name = models.CharField(max_length = 255, choices=ICON_NAME_CHOICE, default=None, null=True)

    def __str__(self) -> str:
        return self.name

class Page (models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    content = models.TextField(null=True)
    type = models.ForeignKey(Type, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.name

class Attribute(models.Model):
    object_name = models.CharField(max_length=255)
    attribute_name = models.CharField(max_length=255)
    attribute_value = models.DecimalField(max_digits = 14, decimal_places=2)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return 'object name: ' + self.object_name + ',  attribute: ' + self.attribute_name + ',  value: ' + str(self.attribute_value)