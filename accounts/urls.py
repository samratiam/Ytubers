from urllib.parse import urlparse
from . import views
from django.urls import path

urlpatterns = [
    path('login/', views.login, name = "login"),
    path('register/', views.register, name = "register"),
    path('logout/', views.logout_user, name = "logout"), #avoid views function named "logout"
    path('dashboard/', views.dashboard, name = "dashboard"),
]