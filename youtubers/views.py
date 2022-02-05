from django.shortcuts import render
from .models import Youtuber

def youtubers(request):
    tubers = Youtuber.objects.order_by('-created_date')
    data = {
        'tubers': tubers,
    }
    return render(request, 'youtubers/youtubers.html', data)

def youtubers_detail(request):
    pass

def search(request):
    pass


