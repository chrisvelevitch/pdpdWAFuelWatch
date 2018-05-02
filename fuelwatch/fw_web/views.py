from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('<h1>Hello views</h1>')

def prices(request):
    return render(request, 'prices.html')