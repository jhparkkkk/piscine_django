from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def init(request):
    return HttpResponse('OK')
