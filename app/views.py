from django.shortcuts import render
from .models import Banco, Usuario
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

@login_required
def indexUser(request):
    return render(request, 'app/indexUser.html')

def register(request):
    return render(request, 'registration/register.html')

def index(request):
    return render(request, 'app/index.html')

def administrador(request):
    Usuario = Usuario.objects.all()
    data = {
        'Usuario': Usuario
    }
    return render(request, 'app/administrador.html')