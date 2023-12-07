from django.urls import path

from . import views

urlpatterns = [
    path('3', views.get_3),
    path('4', views.get_4),
    path('any/<int:num>', views.get_number),
    # if an int doesn't match, send it as a string
    path('any/<num>', views.get_number),
]
