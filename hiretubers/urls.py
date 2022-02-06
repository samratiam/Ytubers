import imp
from django.urls import path,include
from . import views

urlpatterns = [
    path("hiretuber/",views.hiretuber,name="hiretuber"),
]