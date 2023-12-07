from django.shortcuts import render

# there's no Django built-in way to reflect urlpatterns
endpoints = [
    { 'display': '/number/3', 'path': '/number/3' },
    { 'display': '/number/4', 'path': '/number/4' },
    { 'display': '/number/any/*', 'path': '/number/any/42' },
]

def index(request):
    context = { 'endpoints': endpoints }
    return render(request, 'home/index.html', context)
