from django.shortcuts import render, redirect
from .models import Banco
# from .forms import CustomUserCreationForm

# Create your views here.

def intranet(request):
    return render(request, 'app/intranet.html')

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }
    return render(request, 'registration/register.html', data)

def index(request):
    return render(request, 'app/index.html')