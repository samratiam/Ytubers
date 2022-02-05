from django.shortcuts import redirect, render
from django.contrib.auth import logout

# Create your views here.
def login(request):
    return render(request,'accounts/login.html')

def register(request):
    return render(request,'accounts/register.html')


def logout_user(request):
    logout(request)
    return redirect('home')

def dashboard(request):
    return render(request,'accounts/dashboard.html')

