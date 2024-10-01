from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Productos
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

@csrf_exempt
def index(request, id=None):
    
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass
    if request.method == 'DELETE':
        pass
    if request.method == 'PUT':
        pass
    if request.method == 'PATCH':
        pass
