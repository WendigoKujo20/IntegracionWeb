from django.shortcuts import render
from django.http import request

# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def informacion(request):
    return render(request, 'app/informacion.html')