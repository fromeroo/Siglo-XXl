from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario, Proveedor, Menu, Caja, Mesa
from .forms import CustomUserCreationForm 
from .forms import CustomProveedorCreationForm 
from .forms import CustomMenusCreationForm 
from .forms import CustomCajasCreationForm 
from .forms import CustomMesasCreationForm 
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
    return render(request, 'app/administrador/usuarios/indexUser.html', data)

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

    return render(request, 'app/administrador/usuarios/registroUser.html', data)

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
    return render(request, 'app/administrador/usuarios/editarUser.html', data)

def eliminar_usuario(request, id):
    usuario = get_object_or_404(User, id=id)
    usuario.delete()
    messages.success(request, "¡El usuario ha sido desactivado exitosamente!")
    return redirect(to="indexUser")


def indexProveedores(request):
    proveedores = Proveedor.objects.all()
    data = {
        'Proveedores': proveedores
    }
     
    return render(request, 'app/administrador/proveedores/indexProveedores.html', data)

def registroProveedores(request):
    data = {
        'form': CustomProveedorCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomProveedorCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "¡El proveedor ha sido registrado exitosamente!")
            return redirect(to="indexProveedores")
        data["form"] = formulario

    return render(request, 'app/administrador/proveedores/registroProveedores.html', data)

def modificarProveedores(request, id):
    proveedor = get_object_or_404(Proveedor, id_proveedor=id)

    data = {
        'form': CustomProveedorCreationForm(instance=proveedor)
    }

    if request.method == 'POST':
        formulario = CustomProveedorCreationForm(data=request.POST, instance=proveedor)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "¡El proveedor ha sido modificado exitosamente!")
            return redirect(to='indexProveedores')
        data['form'] = formulario
    return render(request, 'app/administrador/proveedores/editarProveedores.html', data)

def indexMenus(request):
    menus = Menu.objects.all()
    data = {
        'Menus': menus
    }
     
    return render(request, 'app/administrador/menus/indexMenus.html', data)

def registroMenus(request):
    data = {
        'form': CustomMenusCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomMenusCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "¡El menu ha sido registrado exitosamente!")
            return redirect(to="indexMenus")
        data["form"] = formulario

    return render(request, 'app/administrador/menus/registroMenus.html', data)

def modificarMenus(request, id):
    menu = get_object_or_404(Menu, id_menu=id)

    data = {
        'form': CustomMenusCreationForm(instance=menu)
    }

    if request.method == 'POST':
        formulario = CustomMenusCreationForm(data=request.POST, instance=menu)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "¡El menu ha sido modificado exitosamente!")
            return redirect(to='indexMenus')
        data['form'] = formulario
    return render(request, 'app/administrador/menus/editarMenus.html', data)

def indexProductos(request):
     
     
    return render(request, 'app/indexProductos.html')


def indexRecetas(request):
     
     
    return render(request, 'app/indexRecetas.html')


def indexMesas(request):
    mesas = Mesa.objects.all()
    data = {
        'Mesas': mesas
    }
     
    return render(request, 'app/administrador/mesas/indexMesas.html', data)

def registroMesas(request):
    data = {
        'form': CustomMesasCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomMesasCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "¡La Mesa ha sido registrada exitosamente!")
            return redirect(to="indexMesas")
        data["form"] = formulario

    return render(request, 'app/administrador/mesas/registroMesas.html', data)

def modificarMesas(request, id):
    mesas = get_object_or_404(Mesa, id_mesa=id)

    data = {
        'form': CustomMesasCreationForm(instance=mesas)
    }

    if request.method == 'POST':
        formulario = CustomMesasCreationForm(data=request.POST, instance=mesas)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "¡La mesa ha sido modificada exitosamente!")
            return redirect(to='indexMesas')
        data['form'] = formulario
    return render(request, 'app/administrador/mesas/editarMesas.html', data)

def indexPedidosProveedor(request):
     
     
    return render(request, 'app/indexPedidosProveedor.html')


def indexGestionCajas(request):
    cajas = Caja.objects.all()
    data = {
        'Cajas': cajas
    }  
     
    return render(request, 'app/administrador/gestion-cajas/indexCajas.html', data)

def registroGestionCajas(request):
    data = {
        'form': CustomCajasCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomCajasCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "¡La Caja ha sido registrada exitosamente!")
            return redirect(to="indexGestionCajas")
        data["form"] = formulario

    return render(request, 'app/administrador/gestion-cajas/registroCajas.html', data)

def modificarGestionCajas(request, id):
    caja = get_object_or_404(Caja, id_caja=id)

    data = {
        'form': CustomCajasCreationForm(instance=caja)
    }

    if request.method == 'POST':
        formulario = CustomCajasCreationForm(data=request.POST, instance=caja)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "La Caja ha sido modificada exitosamente!")
            return redirect(to='indexGestionCajas')
        data['form'] = formulario
    return render(request, 'app/administrador/gestion-cajas/editarMenus.html', data)

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

# DASHBOARD

def dashboard(request):
     
     
    return render(request, 'app/dashboard.html')




    