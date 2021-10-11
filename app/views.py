from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario, Proveedor, Receta, Menu, Caja, Mesa, InventarioInsumo, Insumo, Factura, OrdenComida
from .forms import CustomUserCreationForm, CustomProveedorCreationForm, CustomInsumoCreationForm, CustomRecetaCreationForm, \
    CustomMenusCreationForm, CustomCajasCreationForm, CustomMesasCreationForm, CustomInventarioInsumoCreationForm, \
    CustomFacturaCreationForm
    
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User

from django.shortcuts import render
from django.db import connection

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
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("PKG_PROVEEDOR.listarProveedor", [out_cur])

    lista= []
    for fila in out_cur:
        lista.append(fila)

    data = {
        'Proveedores': lista
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
    
def indexInsumos(request):
    insumos = Insumo.objects.all()
    data = {
        'Insumos': insumos
    }
     
    return render(request, 'app/administrador/insumos/indexInsumos.html', data)

def registroInsumos(request):
    data = {
        'form': CustomInsumoCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomInsumoCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "¡El insumo ha sido registrado exitosamente!")
            return redirect(to="indexInsumos")
        data["form"] = formulario

    return render(request, 'app/administrador/insumos/registroInsumos.html', data)

def modificarInsumos(request, id):
    insumo = get_object_or_404(Insumo, id_ins=id)

    data = {
        'form': CustomInsumoCreationForm(instance=insumo)
    }

    if request.method == 'POST':
        formulario = CustomInsumoCreationForm(data=request.POST, instance=insumo)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "¡El insumo ha sido modificado exitosamente!")
            return redirect(to='indexInsumos')
        data['form'] = formulario
    return render(request, 'app/administrador/insumos/editarInsumos.html', data)

def indexRecetas(request):
    recetas = Receta.objects.all()
    data = {
        'Recetas': recetas
    }
     
    return render(request, 'app/administrador/recetas/indexRecetas.html', data)

def registroRecetas(request):
    data = {
        'form': CustomRecetaCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomRecetaCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "¡Receta creada exitosamente!")
            return redirect(to="indexRecetas")
        data["form"] = formulario

    return render(request, 'app/administrador/recetas/registroRecetas.html', data)

def modificarRecetas(request, id):
    receta = get_object_or_404(Receta, id_receta=id)

    data = {
        'form': CustomRecetaCreationForm(instance=receta)
    }

    if request.method == 'POST':
        formulario = CustomRecetaCreationForm(data=request.POST, instance=receta)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "¡Receta modificada exitosamente!")
            return redirect(to='indexRecetas')
        data['form'] = formulario
    return render(request, 'app/administrador/recetas/editarRecetas.html', data)


def indexPedidosProveedor(request):
     
    return render(request, 'app/administrador/pedidos-proveedor/indexPedidosProveedor.html')


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
    return render(request, 'app/administrador/gestion-cajas/editarCajas.html', data)

def indexGestionCajaFinanzas(request):
    cajas = Caja.objects.all()
    data = {
        'Cajas': cajas
    }
     
    return render(request, 'app/finanzas/cajas/indexGestionCajaFinanzas.html', data)

# BODEGA

def indexStockProductos(request):
    insumo = InventarioInsumo.objects.all()
    data = {
        'Insumos': insumo
    }
     
    return render(request, 'app/bodega/stock-productos/indexStockProductos.html', data)

def registroStockProductos(request):
    data = {
        'form': CustomInventarioInsumoCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomInventarioInsumoCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "¡El producto ha sido registrado exitosamente!")
            return redirect(to="indexStockProductos")
        data["form"] = formulario

    return render(request, 'app/bodega/stock-productos/registroStockProductos.html', data)

def modificarStockProductos(request, id):
    insumo = get_object_or_404(InventarioInsumo, id_inv_ins=id)

    data = {
        'form': CustomInventarioInsumoCreationForm(instance=insumo)
    }

    if request.method == 'POST':
        formulario = CustomInventarioInsumoCreationForm(data=request.POST, instance=insumo)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "¡El producto ha sido modificado exitosamente!")
            return redirect(to='indexStockProductos')
        data['form'] = formulario
    return render(request, 'app/bodega/stock-productos/editarStockProductos.html', data)


# FINANZAS

def indexGestionFacturas(request):
    factura = Factura.objects.all()
    data = {
        'Facturas': factura
    }

    return render(request, 'app/finanzas/facturas/indexFacturas.html', data)


def registroGestionFacturas(request):
    data = {
        'form': CustomFacturaCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomFacturaCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "¡La factura ha sido registrado exitosamente!")
            return redirect(to="indexGestionFacturas")
        data["form"] = formulario

    return render(request, 'app/finanzas/facturas/registroFacturas.html', data)

def modificarGestionFacturas(request, id):
    factura = get_object_or_404(Factura, id_factura=id)

    data = {
        'form': CustomFacturaCreationForm(instance=factura)
    }

    if request.method == 'POST':
        formulario = CustomFacturaCreationForm(data=request.POST, instance=factura)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "La factura ha sido modificado exitosamente!")
            return redirect(to='indexGestionFacturas')
        data['form'] = formulario
    return render(request, 'app/finanzas/facturas/editarFacturas.html', data)



def indexDetalleUtilidades(request):
     
     
    return render(request, 'app/indexDetalleUtilidades.html')

# CAJA

def indexPagoEfectivo(request):
    mesa = Mesa.objects.all()
    data = {
        'Mesas': mesa
    }

    return render(request, 'app/caja/pago-efectivo/indexPagoEfectivo.html', data)

# COCINA

def indexTablero(request):
    ordenComida = OrdenComida.objects.all()
    data = {
        'OrdenComida': ordenComida
    }
     
    return render(request, 'app/cocina/tablero/indexTablero.html', data)

# DASHBOARD

def dashboard(request):
     
     
    return render(request, 'app/dashboard.html')




    