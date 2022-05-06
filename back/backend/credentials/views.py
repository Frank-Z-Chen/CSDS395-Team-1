from cgitb import reset
import imp
from unittest import result
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.db.models import Q
from django.db.models import F
from django.db.models import Value, Func
from django.db.models.functions import Concat
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from credentials.models import login_credentials

# Create your views here.
def say_hello(request):
    queryset = login_credentials.objects.annotate(
            # concat
            full_credentials = Concat(Value('user name: ') ,'user_name', Value(', password: '), 'pass_word', function = 'CONCAT')
        )
    #pull data from db
    #transform 
    #send email
    return render(request, 'hello.html', {'name': 'David', 'result': list(queryset)})