from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest

def get_number(num):
    if isinstance(num, int):
        return HttpResponse(str(num))
    else:
        return HttpResponseBadRequest('Numbers must be whole numbers (integers)')

def get_3(request):
    return get_number(3)
