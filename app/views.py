from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario, Proveedor, Receta, Menu, Caja, Mesa, InventarioInsumo, Insumo, Factura, OrdenComida
from .forms import CustomUserCreationForm, CustomProveedorCreationForm, CustomInsumoCreationForm, CustomRecetaCreationForm, \
    CustomMenusCreationForm, CustomCajasCreationForm, CustomMesasCreationForm, CustomInventarioInsumoCreationForm, \
    CustomFacturaCreationForm
    
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User

from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection

import cx_Oracle

# Create your views here.

@login_required
def indexUser(request):
    usuarios = User.objects.all()
    data = {
        'Usuarios': usuarios
    }
    return render(request, 'app/administrador/usuarios/indexUser.html', data)


@login_required
def register(request):
    return render(request, 'registration/register.html')


@login_required
def index(request):
    return render(request, 'app/index.html')


@login_required
def administrador(request):
    usuario = Usuario.objects.all()
    data = {
        'Usuario': usuario
    }
    return render(request, 'app/administrador.html', data)


@login_required
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


@login_required
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


@login_required
def eliminar_usuario(request, id):
    usuario = get_object_or_404(User, id=id)
    usuario.delete()
    messages.success(request, "¡El usuario ha sido desactivado exitosamente!")
    return redirect(to="indexUser")

@login_required
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


@login_required
def registroProveedores(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    out_cur_two = django_cursor.connection.cursor()

    cursor.callproc("PKG_DIRECCION.listarComunas", [out_cur])
    cursor.callproc("PKG_DIRECCION.listarTipoDireccion", [out_cur_two])

    lista= []
    for fila in out_cur:
        lista.append(fila)

    lista_tipo_direccion = []
    for fila in out_cur_two:
        lista_tipo_direccion.append(fila)

    data = {
        'Comunas': lista,
        'TipoDirecciones': lista_tipo_direccion
    }
     

    return render(request, 'app/administrador/proveedores/registroProveedores.html', data)

def crearProveedor(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    # out_cur = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)

    rut = int(request.GET["p_rut"])
    dv = request.GET["p_dv"]
    razon_social = request.GET["p_razon_social"]
    nombre_corto = request.GET["p_nom_corto"]
    telefono = request.GET["p_telefono"]
    correo = request.GET["p_correo"]
    id_giro = int(request.GET["p_id_giro"])
    direccion = request.GET["p_direccion"]
    numero_dirrecion = int(request.GET["p_num_dir"])
    numero_casa = int(request.GET["p_nro_casa"])
    tipo_direccion = int(request.GET["p_tipo_dir"])
    id_comuna= int(request.GET["p_id_com"])
    

    cursor.callproc("PKG_PROVEEDOR.crearProveedores", [rut, dv, razon_social, nombre_corto, telefono, correo, id_giro, direccion, numero_dirrecion, numero_casa, tipo_direccion, id_comuna, salida])
    
    if salida == 1:
        # ACA ES EL MENSAJE DE ERROR
        return redirect('indexProveedores')
    else:
        messages.success(request, "¡El Proveedor ha sido registrado exitosamente!")
        return redirect('indexProveedores')


@login_required
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


def eliminarProveedores(request, id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    # out_cur = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)

    id_proveedor = int(id)

    cursor.callproc("PKG_PROVEEDOR.eliminarProveedor", [id_proveedor, salida])
    
    messages.success(request, "¡El proveedor ha sido eliminado exitosamente!")
    return redirect(to="indexProveedores")


@login_required
def indexMenus(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("PKG_MENU.listarMenu", [out_cur])

    lista= []
    for fila in out_cur:
        lista.append(fila)

    data = {
        'Menus': lista
    }
     
    return render(request, 'app/administrador/menus/indexMenus.html', data)

def crearMenus(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    # out_cur = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)

    nro_menu = int(request.GET["p_nro_menu"])
    nombre_menu = request.GET["p_nom_menu"]

    cursor.callproc("PKG_MENU.crearMenu", [nro_menu, nombre_menu, salida])

    if salida == 1:
        # ACA ES EL MENSAJE DE ERROR
        return redirect('indexMenus')
    else:
        messages.success(request, "¡El Menu ha sido registrado exitosamente!")
        return redirect('indexMenus')

@login_required
def registroMenus(request):
   
    return render(request, 'app/administrador/menus/registroMenus.html')


@login_required
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


@login_required    
def indexInsumos(request):
    insumos = Insumo.objects.all()
    data = {
        'Insumos': insumos
    }
     
    return render(request, 'app/administrador/insumos/indexInsumos.html', data)


@login_required
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


@login_required
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


@login_required
def indexRecetas(request):
    recetas = Receta.objects.all()
    data = {
        'Recetas': recetas
    }
     
    return render(request, 'app/administrador/recetas/indexRecetas.html', data)


@login_required
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


@login_required
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



@login_required
def indexPedidosProveedor(request):
     
    return render(request, 'app/administrador/pedidos-proveedor/indexPedidosProveedor.html')



@login_required
def indexMesas(request):
    mesas = Mesa.objects.all()
    data = {
        'Mesas': mesas
    }
     
    return render(request, 'app/administrador/mesas/indexMesas.html', data)


@login_required
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


@login_required
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


@login_required
def indexGestionCajas(request):
    cajas = Caja.objects.all()
    data = {
        'Cajas': cajas
    } 
     
    return render(request, 'app/administrador/gestion-cajas/indexCajas.html', data)


@login_required
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


@login_required
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


@login_required
def indexGestionCajaFinanzas(request):
    cajas = Caja.objects.all()
    data = {
        'Cajas': cajas
    }
     
    return render(request, 'app/finanzas/cajas/indexGestionCajaFinanzas.html', data)

# BODEGA


@login_required
def indexStockProductos(request):
    insumo = InventarioInsumo.objects.all()
    data = {
        'Insumos': insumo
    }
     
    return render(request, 'app/bodega/stock-productos/indexStockProductos.html', data)


@login_required
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


@login_required
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


@login_required
def indexGestionFacturas(request):
    factura = Factura.objects.all()
    data = {
        'Facturas': factura
    }

    return render(request, 'app/finanzas/facturas/indexFacturas.html', data)



@login_required
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


@login_required
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



@login_required
def indexInformes(request):
     
    return render(request, 'app/finanzas/informes/indexInformes.html')

# CAJA


@login_required
def indexPagoEfectivo(request):
    mesa = Mesa.objects.all()
    data = {
        'Mesas': mesa
    }

    return render(request, 'app/caja/pago-efectivo/indexPagoEfectivo.html', data)

# COCINA


@login_required
def indexTablero(request):
    ordenComida = OrdenComida.objects.all()
    data = {
        'OrdenComida': ordenComida
    }
     
    return render(request, 'app/cocina/tablero/indexTablero.html', data)

# DASHBOARD


@login_required
def dashboard(request):
     
     
    return render(request, 'app/dashboard.html')

# TABLET CLIENTE
def clienteMenu(request):
    messages.success(request, "¡!")
    return render(request, 'app/cliente/clienteMenu.html')

def detalleCliente(request):
    messages.success(request, "¡!")
    return render(request, 'app/cliente/detalleCliente.html')

def pagoCliente(request):
    messages.success(request, "¡!")
    return render(request, 'app/cliente/pagoCliente.html')




    