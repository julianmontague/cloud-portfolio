from django.urls import path

from . import views

urlpatterns = [
    path('3', views.get_3),
]
