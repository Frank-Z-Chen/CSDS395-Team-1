from dataclasses import field
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from. import models
# Register your models here.


class summer_admin(SummernoteModelAdmin, admin.ModelAdmin):
    #autocomplete_fields = ['type']
    list_display = ['name', 'type']
    summernote_fields = 'content,'
    prepopulated_fields = {
        'slug' : ['name']
    }
    list_per_page = 10
    search_fields = ['name__istartswith']

class type_admin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ['name__istartswith', 'icon_name__istartswith']

class attribute_admin(admin.ModelAdmin):
    list_display = ['object_name', 'attribute_name', 'attribute_value']
    search_fields = ['object_name__istartswith', 'attribute_name__istartswith', 'attribute_value']
    list_per_page = 10


admin.site.register(models.Page, summer_admin)
admin.site.register(models.Type, type_admin)
admin.site.register(models.Attribute, attribute_admin)


