from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def func(request):
    return HttpResponse("<h1> function is called here </h1>") 