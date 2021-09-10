from django.shortcuts import render
from .models import Usuario
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

@login_required
def indexUser(request):
    usuario = Usuario.objects.all()
    data = {
        'Usuario': usuario
    }
    return render(request, 'app/indexUser.html', data)

def register(request):
    return render(request, 'registration/register.html')

def index(request):
    return render(request, 'app/index.html')

def administrador(request):
    usuario = Usuario.objects.all()
    data = {
        'Usuario': usuario
    }
    return render(request, 'app/administrador.html', data)

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "El usuario ha sido registrado exitosamente!")
        data["form"] = formulario

    return render(request, 'registration/registro.html', data)
