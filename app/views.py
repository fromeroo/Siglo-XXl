from django.shortcuts import render

# Create your views here.

def intranet(request):
    return render(request, 'app/intranet.html')

def login(request):
    return render(request, 'app/login.html')