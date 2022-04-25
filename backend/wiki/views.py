import os
from fileinput import filename
from http.client import responses
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from wiki.models import Page,Type, Attribute
from wiki import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.exceptions import UnsupportedMediaType, NotAcceptable, APIException
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
import sp.util
from . import util
import json
import base64


pwd = sp.util.sp_address_extension(os.getcwd()) 

# Create your views here.
@api_view(['GET', 'POST'])
def type_list(request):
    if request.method == 'GET':
        queryset = Type.objects.all()
        serializer = serializers.Type_serializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = serializers.Type_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

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

class OCR_data:
    def __init__(self):
        self.json = None
        self.image = None

    def get_raw_data(self, name, type_name):
        #run the getdata.py
        os.system("python %s" %('sp/getdata.py' + ' ' +  '{0}.png'.format(name) + ' {0}'.format(type_name)))
        csv_path = 'sp/roughdata/' + '{0}_{1}'.format(type_name, name) + '_temp_rough.csv'
        js_path = 'sp/roughdata/' + '{0}_{1}'.format(type_name, name) + '_temp_rough.json'
        util.make_json(csv_path, js_path)
        f = open('sp/roughdata/{0}_{1}_temp_rough.json'.format(type_name, name))
        self.json = json.load(f)

        with open('sp/temp/{0}_{1}_temp_mark.png'.format(type_name, name), "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        self.image = encoded_string


class OcrView(APIView):
    renderer_classes = [JSONRenderer]
    
    def post(self, request, type_name, page_slug):
        try:
            temp_image = request.data['file']
            name = page_slug
            type_name = type_name
            # print(type(request.data['file']))

        except KeyError:
            raise UnsupportedMediaType('only accept a form with files')
        

        #create the ocr class
        if os.path.isfile('sp/figure/{0}.png'.format(name)):
            os.remove('sp/figure/{0}.png'.format(name))
        path = default_storage.save('{0}.png'.format(name), ContentFile(temp_image.read()))

        ocr = OCR_data()
        ocr.get_raw_data(name, type_name)
        serializer = serializers.ocr_serializer(ocr)

        test = {"a":"a"}
        # print(serializer.data)
        return Response(serializer.data)


def generate_ocr_response(type_name, name):
    #run the getdata_continue.py
    os.system("python %s" %('sp/getdata_continue.py' + ' ' +  '{0}'.format(name) + ' ' + '{0}'.format(type_name)))
    #after the process finished, read the opt data and add tuples to database
    opt_file_path = 'sp/roughdata/{0}_{1}_temp_rough_opt.csv'.format(type_name, name)
    dict = util.csv_to_dict_opt_only(opt_file_path)
    
    #generate tuples in the database
    for i in range(len(dict['ATT'])):
        page_object = Page.objects.filter(slug=name).first()

        # det the default for update
        new_object_name = name
        new_attribute_name=dict['ATT'][i]
        new_attribute_value=dict['CON'][i]
        new_page=page_object

        Attribute.objects.update_or_create(
            object_name=name,
            attribute_name=dict['ATT'][i],
            attribute_value=dict['CON'][i],
            page=page_object,
            
            #for update if match exists
            defaults={
                'object_name':new_object_name,
                'attribute_name':new_attribute_name,
                'attribute_value':new_attribute_value,
                'page':new_page
            }
        )

        #finish updating the database, return to the page detail!




class OcrResponseView(APIView):
    def post(self, request, type_name, page_slug):
        try:
            json_file = request.body.decode('utf-8') 
            name = page_slug
            type_name = type_name

        except Exception:
            raise APIException('something went wrong')

        #save the json file
        path_json = 'sp/roughdata/{0}_{1}_temp_rough_response.json'.format(type_name, name)
        #convert the string to json
        json_file = json.loads(json_file)
        with open(path_json, 'w') as f:
            json.dump(json_file, f)

        #convert it as csv file
        path_csv = 'sp/data/{0}_{1}_temp_learn.csv'.format(type_name,name)
        util.make_csv(path_json, path_csv)

        generate_ocr_response(type_name, name)

        page = get_object_or_404(Page, slug = page_slug)
        serializer = serializers.page_serializer(instance=page)
        return Response(serializer.data)


    

