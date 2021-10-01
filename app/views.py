from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User

# Create your views here.

@login_required
def indexUser(request):
    usuarios = User.objects.all()
    data = {
        'Usuarios': usuarios
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
            messages.success(request, "¡El usuario ha sido registrado exitosamente!")
            return redirect(to="indexUser")
        data["form"] = formulario

    return render(request, 'registration/registro.html', data)

def modificar_usuario(request, id):
    usuario = get_object_or_404(User, id=id)

    data = {
        'form': CustomUserCreationForm(instance=usuario)
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "¡El usuario ha sido modificado exitosamente!")
            return redirect(to='indexUser')
        data['form'] = formulario
    return render(request, 'registration/editarUsuario.html', data)

def eliminar_usuario(request, id):
    usuario = get_object_or_404(User, id=id)
    usuario.delete()
    messages.success(request, "¡El usuario ha sido desactivado exitosamente!")
    return redirect(to="indexUser")


def indexProveedores(request):
     
     
    return render(request, 'app/indexProveedores.html')


def indexMenus(request):
     
     
    return render(request, 'app/indexMenus.html')


def indexProductos(request):
     
     
    return render(request, 'app/indexProductos.html')


def indexRecetas(request):
     
     
    return render(request, 'app/indexRecetas.html')


def indexMesas(request):
     
     
    return render(request, 'app/indexMesas.html')


def indexPedidosProveedor(request):
     
     
    return render(request, 'app/indexPedidosProveedor.html')


def indexGestionCajas(request):
     
     
    return render(request, 'app/indexGestionCajas.html')

# BODEGA

def indexStockProductos(request):
     
     
    return render(request, 'app/indexStockProductos.html')

# FINANZAS

def indexGestionCajaFinanzas(request):
     
     
    return render(request, 'app/indexGestionCajaFinanzas.html')

def indexGestionFacturas(request):
     
     
    return render(request, 'app/indexGestionFacturas.html')

def indexDetalleUtilidades(request):
     
     
    return render(request, 'app/indexDetalleUtilidades.html')

# CAJA

def indexPagoEfectivo(request):
     
     
    return render(request, 'app/indexPagoEfectivo.html')

# COCINA

def indexTablero(request):
     
     
    return render(request, 'app/indexTablero.html')




    