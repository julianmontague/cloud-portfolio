from django.http import HttpResponse, HttpResponseBadRequest

def get_number(request, num):
    if isinstance(num, int):
        return HttpResponse(str(num))
    else:
        return HttpResponseBadRequest('Numbers must be whole numbers (integers) greater than zero')

def get_3(request):
    return get_number(request, 3)

def get_4(request):
    return get_number(request, 4)
