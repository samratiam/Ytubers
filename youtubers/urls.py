from django.urls import path
from . import views

urlpatterns = [
    path('youtubers/', views.youtubers, name="youtubers"),
    path('<int:id>/',views.youtubers_detail, name = "youtubers_detail"),
    path('search/', views.search, name="search"),
]