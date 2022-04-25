from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.

def hello_world(request):
    return HttpResponse('Hello World!')