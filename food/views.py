from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def veg(request):
    return HttpResponse('this is the veg list:')