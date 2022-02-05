from django.shortcuts import get_object_or_404, render
from .models import Youtuber

def youtubers(request):
    tubers = Youtuber.objects.order_by('-created_date')
    data = {
        'tubers': tubers,
    }
    return render(request, 'youtubers/youtubers.html', data)

def youtubers_detail(request,id):
    tuber = get_object_or_404(Youtuber, pk=id)
    data = {
        'tuber': tuber
    }
    return render(request, 'youtubers/youtuber_detail.html', data)


def search(request):
    pass


