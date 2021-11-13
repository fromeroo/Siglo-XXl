from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario, Proveedor, Receta, Menu, Caja, Mesa, InventarioInsumo, Insumo, Factura, OrdenComida
from .forms import CustomUserCreationForm, CustomProveedorCreationForm, CustomInsumoCreationForm, CustomRecetaCreationForm, \
    CustomMenusCreationForm, CustomCajasCreationForm, CustomMesasCreationForm, CustomInventarioInsumoCreationForm, \
    CustomFacturaCreationForm, CrearReservaForm
    
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User

from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection

import cx_Oracle
from datetime import datetime


@login_required
def indexUser(request):
    usuarios = User.objects.all()
    data = {
        'Usuarios': usuarios
    }
    return render(request, 'app/administrador/usuarios/indexUser.html', data)

def listarRolesUsuario(request, id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    out_cur_two = django_cursor.connection.cursor()

    cursor.callproc("PKG_USER_GROUP.listarGroup", [out_cur])
    cursor.callproc("PKG_USER_GROUP.buscarUserGroup", [id, out_cur_two])

    lista= []
    for fila in out_cur:
        lista.append(fila)
    
    lista_user_group = []
    for fila in out_cur_two:
        lista_user_group.append(fila)
    
    data = {
        'Grupos': lista,
        'IdUser': id,
        'UserGroup': lista_user_group
    }

    print(lista_user_group)
     
    return render(request, 'app/administrador/usuarios/listarRolesUsuario.html', data)

def cambiarRolUsuario(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)

    p_id_user = int(request.GET["p_id_user"])
    p_id_oc = int(request.GET["p_id_oc"])

    cursor.callproc("PKG_USER_GROUP.actualizarUserGroup", [p_id_user, p_id_oc, salida])
    
    if salida.getvalue() == 1:
        messages.success(request, "¡El rol de usuario ha sido editado exitosamente!")
        return redirect('indexUser')
    else:
        messages.error(request, "¡Ha ocurrido un error, favor contactar con administrador!")
        return redirect('indexUser')

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
    out_cur_three = django_cursor.connection.cursor()

    cursor.callproc("PKG_DIRECCION.listarComunas", [out_cur])
    cursor.callproc("PKG_DIRECCION.listarTipoDireccion", [out_cur_two])
    cursor.callproc("PKG_PROVEEDOR.listarGiros", [out_cur_three])

    lista= []
    for fila in out_cur:
        lista.append(fila)

    lista_tipo_direccion = []
    for fila in out_cur_two:
        lista_tipo_direccion.append(fila)

    lista_giro = []
    for fila in out_cur_three:
        lista_giro.append(fila)

    data = {
        'Comunas': lista,
        'TipoDirecciones': lista_tipo_direccion,
        'Giros': lista_giro
    }
     
    return render(request, 'app/administrador/proveedores/registroProveedores.html', data)

@login_required
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
        messages.success(request, "¡El Proveedor ha sido registrado exitosamente!")
        return redirect('indexProveedores')
    else:
        messages.error(request, "¡Ha ocurrido un error, favor contactar con administrador!")
        return redirect('indexProveedores')

@login_required
def actualizarProveedores(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    # out_cur = django_cursor.connection.cursor()

    id_proveedor = int(request.GET["p_id"])
    razon_social = request.GET["p_razon_social"]
    nombre_corto = request.GET["p_nom_corto"]
    telefono = request.GET["p_telefono"]
    correo = request.GET["p_correo"]
    id_giro = int(request.GET["p_id_giro"])
    direccion = request.GET["p_direccion"]
    numero_direcion = request.GET["p_num_dir"]
    numero_casa = int(request.GET["p_nro_casa"])
    tipo_direccion = int(request.GET["p_tipo_dir"])
    id_comuna= int(request.GET["p_id_com"])
    salida = cursor.var(cx_Oracle.NUMBER)

    cursor.callproc("PKG_PROVEEDOR.modificarProveedor", [id_proveedor, razon_social, nombre_corto, telefono, correo, id_giro, direccion, numero_direcion, numero_casa, tipo_direccion, id_comuna, salida])
    
    if salida.getvalue() == 1:
        # ACA ES EL MENSAJE DE ERROR
        messages.success(request, "¡El Proveedor ha sido modificado exitosamente!")
        return redirect('indexProveedores')
    else:
        messages.error(request, "¡Ha ocurrido un error, favor contactar con administrador!")
        return redirect('indexProveedores')

@login_required
def modificarProveedores(request, id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    out_cur_two = django_cursor.connection.cursor()
    out_cur_three = django_cursor.connection.cursor()
    out_cur_four = django_cursor.connection.cursor()

    cursor.callproc("PKG_PROVEEDOR.buscarProveedor", [id, out_cur])
    cursor.callproc("PKG_PROVEEDOR.listarGiros", [out_cur_two])
    cursor.callproc("PKG_DIRECCION.listarComunas", [out_cur_three])
    cursor.callproc("PKG_DIRECCION.listarTipoDireccion", [out_cur_four])

    lista= []
    for fila in out_cur:
        lista.append(fila)

    lista_giro = []
    for fila in out_cur_two:
        lista_giro.append(fila)

    lista_comuna = []
    for fila in out_cur_three:
        lista_comuna.append(fila)

    lista_tipo_direccion = []
    for fila in out_cur_four:
        lista_tipo_direccion.append(fila)

    data = {
        'Proveedor': lista,
        'ListaGiro': lista_giro,
        'ListaComuna': lista_comuna,
        'ListaTipoDireccion': lista_tipo_direccion,
    }
    
    return render(request, 'app/administrador/proveedores/editarProveedores.html', data)

@login_required
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

@login_required
def crearMenus(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    # out_cur = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)

    nro_menu = int(request.GET["p_nro_menu"])
    nombre_menu = request.GET["p_nom_menu"]

    cursor.callproc("PKG_MENU.crearMenu", [nro_menu, nombre_menu, salida])

    res = salida.getvalue()

    if res == 1:
        messages.success(request, "¡El Menu ha sido registrado exitosamente!")
        return redirect('indexMenus')
    else:
        messages.error(request, "¡Ha ocurrido un error, favor contactar con administrador!")
        return redirect('indexMenus')

@login_required
def registroMenus(request):
   
    return render(request, 'app/administrador/menus/registroMenus.html')

@login_required
def modificarMenus(request, id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    id_menu = id

    cursor.callproc("PKG_MENU.buscarMenu", [id_menu, out_cur])

    lista= []
    for fila in out_cur:
        lista.append(fila)

    data = {
        'Menus': lista
    }

    return render(request, 'app/administrador/menus/editarMenus.html', data)

@login_required
def editarMenus(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    # out_cur = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)

    id_menu = int(request.GET["id"])
    nro_menu = int(request.GET["p_nro_menu"])
    nom_menu = request.GET["p_nom_menu"]

    cursor.callproc("PKG_MENU.modificarMenu", [id_menu, nro_menu, nom_menu, salida])
    
    res = salida.getvalue()

    if res == 1:
        messages.success(request, "¡El Menu ha sido editado exitosamente!")
        return redirect('indexMenus')
    else:
        messages.error(request, "¡Ha ocurrido un error, favor contactar con administrador!")
        return redirect('indexMenus')

@login_required
def eliminarMenus(request, id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    # out_cur = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)

    id_menu = int(id)

    cursor.callproc("PKG_MENU.eliminarMenu", [id_menu, salida])
    
    messages.success(request, "¡El menu ha sido eliminado exitosamente!")
    return redirect(to="indexMenus")

@login_required
def indexMenusProductos(request, id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    menu = get_object_or_404(Menu, id_menu=id)

    p_id_menu = menu.id_menu

    cursor.callproc("PKG_MENU.listarDetalleMenu", [p_id_menu, out_cur])

    lista= []
    for fila in out_cur:
        lista.append(fila)

    data = {
        'Menus': lista,
        'id': p_id_menu
    }
     
    return render(request, 'app/administrador/menus/indexMenusProductos.html', data)

@login_required
def registroMenusProductos(request, id):
    menu = get_object_or_404(Menu, id_menu=id)
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("PKG_PRODUCTO.listarProducto", [out_cur])

    lista= []
    for fila in out_cur:
        lista.append(fila)

    data = {
        'id': menu.id_menu,
        'Productos': lista
    }

    return render(request, 'app/administrador/menus/registroMenusProductos.html', data)

@login_required
def crearMenusProductos(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    # out_cur = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)

    p_id_menu = int(request.GET["p_id_menu"])
    p_id_producto = int(request.GET["p_id_producto"])
    p_descripcion = request.GET["p_descripcion"]

    cursor.callproc("PKG_MENU.crearDetalleMenu", [p_id_menu, p_id_producto, p_descripcion, salida])

    res = salida.getvalue()

    if res == 1:
        messages.success(request, "¡El detalle del menu ha sido registrado exitosamente!")
        return redirect('indexMenusProductos', id = str(p_id_menu))
    else:
        messages.error(request, "¡Ha ocurrido un error, favor contactar con administrador!")
        return redirect('indexMenusProductos', id = str(p_id_menu))

@login_required
def modificarMenusProductos(request, id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    out_cur_two = django_cursor.connection.cursor()
    
    id_det_menu = id

    cursor.callproc("PKG_MENU.buscarDetalleMenu", [id_det_menu, out_cur])
    cursor.callproc("PKG_PRODUCTO.listarProducto", [out_cur_two])

    lista= []
    for fila in out_cur:
        lista.append(fila)
    
    lista_productos= []
    for fila in out_cur_two:
        lista_productos.append(fila)

    data = {
        'MenuProductos': lista,
        'Productos' : lista_productos
    }

    return render(request, 'app/administrador/menus/editarMenusProductos.html', data)

@login_required
def editarMenusProductos(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    # out_cur = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)

    p_id_det_menu = int(request.GET["p_id_det_menu"])
    p_id_producto = int(request.GET["p_id_producto"])
    p_descripcion = request.GET["p_descripcion"]

    p_id_menu = request.GET["p_id_menu"]

    cursor.callproc("PKG_MENU.modificarDetalleMenu", [p_id_det_menu, p_id_producto, p_descripcion, salida])
    
    res = salida.getvalue()

    if res == 1:
        messages.success(request, "¡El detalle del menu ha sido editado exitosamente!")
        return redirect('indexMenusProductos', id = p_id_menu)
    else:
        messages.error(request, "¡Ha ocurrido un error, favor contactar con administrador!")
        return redirect('indexMenusProductos', id = p_id_menu)

@login_required    
def indexInsumos(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("PKG_INSUMO.listarInsumo", [out_cur])

    lista= []
    for fila in out_cur:
        lista.append(fila)

    data = {
        'Insumos': lista
    }
     
    return render(request, 'app/administrador/insumos/indexInsumos.html', data)

@login_required
def registroInsumos(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    out_cur_two = django_cursor.connection.cursor()

    cursor.callproc("PKG_INSUMO.listarTipoInsumo", [out_cur])
    cursor.callproc("PKG_INSUMO.listarCategoriaInsumo", [out_cur_two])

    lista_tipo_insumo= []
    for fila in out_cur:
        lista_tipo_insumo.append(fila)

    lista_categoria_insumo = []
    for fila in out_cur_two:
        lista_categoria_insumo.append(fila)

    data = {
        'TipoInsumos': lista_tipo_insumo,
        'CategoriasInsumo': lista_categoria_insumo,
    }
     
    return render(request, 'app/administrador/insumos/registroInsumos.html', data)

@login_required
def crearInsumo(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)

    nombre_insumo = request.GET["p_nom_insumo"]
    tipo_insumo = int(request.GET["p_id_tipo_insumo"])
    categoria_insumo = int(request.GET["p_id_cat_insumo"])

    cursor.callproc("PKG_INSUMO.crearInsumo", [nombre_insumo, tipo_insumo, categoria_insumo, salida])
    
    if salida.getvalue() == 1:
        messages.success(request, "¡El Insumo ha sido creado exitosamente!")
        return redirect('indexInsumos')
    else:
        messages.error(request, "¡Ha ocurrido un error, favor contactar con administrador!")
        return redirect('indexInsumos')

@login_required
def actualizarInsumos(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()

    id_insumo = int(request.GET["p_id_insumo"])
    nombre_insumo = request.GET["p_nom_insumo"]
    tipo_insumo = int(request.GET["p_id_tipo_insumo"])
    categoria_insumo = int(request.GET["p_id_cat_insumo"])

    salida = cursor.var(cx_Oracle.NUMBER)

    cursor.callproc("PKG_INSUMO.modificarInsumo", [id_insumo, nombre_insumo, tipo_insumo, categoria_insumo, salida])
    
    if salida.getvalue() == 1:
        # ACA ES EL MENSAJE DE ERROR
        messages.success(request, "¡El Insumo ha sido modificado exitosamente!")
        return redirect('indexInsumos')
    else:
        messages.error(request, "¡Ha ocurrido un error, favor contactar con administrador!")
        return redirect('indexInsumos')

@login_required
def modificarInsumos(request, id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    out_cur_two = django_cursor.connection.cursor()
    out_cur_three = django_cursor.connection.cursor()
    id_insumo = id

    cursor.callproc("PKG_INSUMO.buscarInsumo", [id_insumo, out_cur])
    cursor.callproc("PKG_INSUMO.listarTipoInsumo", [out_cur_two])
    cursor.callproc("PKG_INSUMO.listarCategoriaInsumo", [out_cur_three])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    lista_tipo_insumo = []
    for fila in out_cur_two:
        lista_tipo_insumo.append(fila)

    lista_categoria_insumo = []
    for fila in out_cur_three:
        lista_categoria_insumo.append(fila)

    data = {
        'Insumo': lista,
        'TipoInsumo': lista_tipo_insumo,
        'CategoriaInsumo': lista_categoria_insumo
    }

    return render(request, 'app/administrador/insumos/editarInsumos.html', data)

@login_required
def eliminarInsumos(request, id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    id_insumo = int(id)

    cursor.callproc("PKG_INSUMO.eliminarInsumo", [id_insumo, salida])
    
    messages.success(request, "¡El insumo ha sido eliminado exitosamente!")
    return redirect(to="indexInsumos")

@login_required
def indexProductos(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("PKG_PRODUCTO.listarProducto", [out_cur])

    lista= []
    for fila in out_cur:
        lista.append(fila)

    data = {
        'Productos': lista
    }

    return render(request, 'app/administrador/productos/indexProductos.html', data)

@login_required
def registroProductos(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    out_cur_two = django_cursor.connection.cursor()
    out_cur_three = django_cursor.connection.cursor()


    cursor.callproc("PKG_PRODUCTO.listarCatProducto", [out_cur])
    cursor.callproc("PKG_PRODUCTO.listarTipoProducto", [out_cur_two])
    cursor.callproc("PKG_RECETA.listarReceta", [out_cur_three])

    lista= []
    for fila in out_cur:
        lista.append(fila)

    lista_tipo_producto = []
    for fila in out_cur_two:
        lista_tipo_producto.append(fila)

    lista_receta = []
    for fila in out_cur_three:
        lista_receta.append(fila)

    data = {
        'Categorias': lista,
        'TipoProductos': lista_tipo_producto,
        'Recetas': lista_receta
    }

    return render(request, 'app/administrador/productos/registroProductos.html', data)

@login_required
def crearProductos(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    # out_cur = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)

    p_nom_producto = request.GET["p_nom_producto"]
    p_precio = int(request.GET["p_precio"])
    p_id_cat = int(request.GET["p_id_cat"])
    p_id_tipo = int(request.GET["p_id_tipo"])
    p_id_receta = int(request.GET["p_id_receta"])

    cursor.callproc("PKG_PRODUCTO.crearProducto", [p_nom_producto, p_precio, p_id_cat, p_id_tipo, p_id_receta, salida])

    res = salida.getvalue()

    if res == 1:
        messages.success(request, "¡El producto ha sido registrado exitosamente!")
        return redirect('indexProductos')
    else:
        messages.error(request, "¡Ha ocurrido un error, favor contactar con administrador!")
        return redirect('indexProductos')

@login_required
def modificarProductos(request, id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    out_cur_two = django_cursor.connection.cursor()
    out_cur_three = django_cursor.connection.cursor()
    out_cur_four = django_cursor.connection.cursor()
    id_producto = id

    cursor.callproc("PKG_PRODUCTO.listarCatProducto", [out_cur])
    cursor.callproc("PKG_PRODUCTO.listarTipoProducto", [out_cur_two])
    cursor.callproc("PKG_RECETA.listarReceta", [out_cur_three])
    cursor.callproc("PKG_PRODUCTO.buscarProducto", [id_producto, out_cur_four])

    lista= []
    for fila in out_cur:
        lista.append(fila)

    lista_tipo_producto = []
    for fila in out_cur_two:
        lista_tipo_producto.append(fila)

    lista_receta = []
    for fila in out_cur_three:
        lista_receta.append(fila)
    
    lista_producto = []
    for fila in out_cur_four:
        lista_producto.append(fila)

    data = {
        'Categorias': lista,
        'TipoProductos': lista_tipo_producto,
        'Recetas': lista_receta,
        'Productos': lista_producto
    }

    return render(request, 'app/administrador/productos/editarProductos.html', data)

@login_required
def editarProductos(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    # out_cur = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)

    p_id_producto = int(request.GET["p_id_producto"])
    p_nom_prod = request.GET["p_nom_prod"]
    p_precio = int(request.GET["p_precio"])
    p_id_cat = int(request.GET["p_id_cat"])
    p_id_tipo = int(request.GET["p_id_tipo"])
    p_id_receta = int(request.GET["p_id_receta"])

    cursor.callproc("PKG_PRODUCTO.modificarProducto", [p_id_producto, p_nom_prod, p_precio, p_id_cat, p_id_tipo, p_id_receta, salida])
    
    res = salida.getvalue()

    if res == 1:
        messages.success(request, "¡El Producto ha sido editado exitosamente!")
        return redirect('indexProductos')
    else:
        messages.error(request, "¡Ha ocurrido un error, favor contactar con administrador!")
        return redirect('indexProductos')

@login_required
def eliminarProductos(request, id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    id_producto = int(id)

    cursor.callproc("PKG_PRODUCTO.eliminarProducto", [id_producto, salida])
    
    messages.success(request, "¡El producto ha sido eliminado exitosamente!")
    return redirect(to="indexProductos")

@login_required
def indexRecetas(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("PKG_RECETA.listarReceta", [out_cur])

    lista= []
    for fila in out_cur:
        lista.append(fila)

    data = {
        'Recetas': lista
    }
     
    return render(request, 'app/administrador/recetas/indexRecetas.html', data)

@login_required
def registroRecetas(request):

    return render(request, 'app/administrador/recetas/registroRecetas.html')

@login_required
def crearRecetas(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    # out_cur = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)

    p_nom_receta = request.GET["p_nom_receta"]
    p_tiempo_prep = int(request.GET["p_tiempo_prep"])
    p_temp_ideal = int(request.GET["p_temp_ideal"])
    p_instrucciones = request.GET["p_instrucciones"]

    cursor.callproc("PKG_RECETA.crearReceta", [p_nom_receta, p_tiempo_prep, p_temp_ideal, p_instrucciones, salida])

    res = salida.getvalue()
    if res == 1:
        messages.success(request, "¡La receta ha sido registrada exitosamente!")
        return redirect('indexRecetas')
    else:
        messages.error(request, "¡Ha ocurrido un error, favor contactar con administrador!")
        return redirect('indexRecetas')

@login_required
def modificarRecetas(request, id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    id_receta = id

    cursor.callproc("PKG_RECETA.buscarReceta", [id_receta, out_cur])

    lista= []
    for fila in out_cur:
        lista.append(fila)

    data = {
        'Recetas': lista
    }
    
    return render(request, 'app/administrador/recetas/editarRecetas.html', data)

def editarRecetas(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    # out_cur = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)

    p_id_receta = int(request.GET["p_id_receta"])
    p_nom_receta = request.GET["p_nom_receta"]
    p_tiempo_prep = int(request.GET["p_tiempo_prep"])
    p_temp_ideal = int(request.GET["p_temp_ideal"])
    p_instrucciones = request.GET["p_instrucciones"]

    cursor.callproc("PKG_RECETA.modificarReceta", [p_id_receta, p_nom_receta, p_tiempo_prep, p_temp_ideal, p_instrucciones, salida])
    
    res = salida.getvalue()

    if res == 1:
        messages.success(request, "¡La Receta ha sido editada exitosamente!")
        return redirect('indexRecetas')
    else:
        messages.error(request, "¡Ha ocurrido un error, favor contactar con administrador!")
        return redirect('indexRecetas')

@login_required
def eliminarRecetas(request, id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    id_receta = int(id)

    cursor.callproc("PKG_RECETA.eliminarReceta", [id_receta, salida])
    
    messages.success(request, "¡La Receta ha sido eliminada exitosamente!")
    return redirect(to="indexRecetas")

@login_required
def indexIngredientesRecetas(request, id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    receta = get_object_or_404(Receta, id_receta=id)

    p_id_receta = receta.id_receta

    cursor.callproc("PKG_RECETA.listarIngredientesReceta", [p_id_receta, out_cur])

    lista= []
    for fila in out_cur:
        lista.append(fila)

    data = {
        'id': p_id_receta,
        'IngredientesRecetas': lista
    }

    return render(request, 'app/administrador/recetas/indexIngredientesRecetas.html', data)

@login_required
def registroIngredientesRecetas(request, id):
    receta = get_object_or_404(Receta, id_receta=id)
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("PKG_INSUMO.listarInsumo", [out_cur])

    lista= []
    for fila in out_cur:
        lista.append(fila)

    data = {
        'id': receta.id_receta,
        'Ingredientes': lista
    }

    return render(request, 'app/administrador/recetas/registroIngredientesRecetas.html', data)

@login_required
def crearIngredientesRecetas(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    # out_cur = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)

    p_id_receta = int(request.GET["p_id_receta"])
    p_id_insumo = int(request.GET["p_id_insumo"])
    p_cant = int(request.GET["p_cant"])

    cursor.callproc("PKG_RECETA.crearRecetaInsumo", [p_id_receta, p_id_insumo, p_cant, salida])

    res = salida.getvalue()

    if res == 1:
        messages.success(request, "¡El Ingrediente de la receta ha sido registrado exitosamente!")
        return redirect('indexIngredientesRecetas', id = str(p_id_receta))
    else:
        messages.error(request, "¡Ha ocurrido un error, favor contactar con administrador!")
        return redirect('indexIngredientesRecetas', id = str(p_id_receta))

@login_required
def indexPedidosProveedor(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("PKG_PEDIDO_INSUMO.listarPedidosNuevos", [out_cur])

    lista= []
    for fila in out_cur:
        lista.append(fila)

    data = {
        'PedidosNuevos': lista
    }

    return render(request, 'app/administrador/pedidos-proveedor/indexPedidosProveedor.html', data)

@login_required
def detallePedidosProveedor(request, id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    id_pedido = id

    cursor.callproc("PKG_PEDIDO_INSUMO.buscarDetPedido", [id_pedido, out_cur])

    lista= []
    for fila in out_cur:
        lista.append(fila)

    data = {
        'DetallePedidos': lista
    }

    return render(request, 'app/administrador/pedidos-proveedor/detallePedidosProveedor.html', data)

@login_required
def autorizarPedidosProveedor(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    # out_cur = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)

    p_id_pedido = int(request.GET["p_id_pedido"])
    p_opcion1 = int(request.GET["p_opcion1"])
    p_opcion2 = int(request.GET["p_opcion2"])

    cursor.callproc("PKG_PEDIDO_INSUMO.autorizarPedidos", [p_id_pedido, p_opcion1, p_opcion2, salida])
    
    if salida.getvalue() == 1:
        messages.success(request, "¡Cambio realizado con exito!")
        return redirect('indexPedidosProveedor')
    else:
        messages.error(request, "¡Ha ocurrido un error, favor contactar con administrador!")
        return redirect('indexPedidosProveedor')

@login_required
def registrarOrdenCompra(request, id):
    
    id_pedido = id

    data = {
        'id': id_pedido,
    }

    return render(request, 'app/administrador/pedidos-proveedor/generarOrdenCompra.html', data)

@login_required
def crearOrdenCompra(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()

    p_neto = int(request.GET["p_neto"])
    p_id_pedido = int(request.GET["p_id_pedido"])
    p_vigencia = int(request.GET["p_vigencia"])
    salida = cursor.var(cx_Oracle.NUMBER)

    cursor.callproc("PKG_ORDEN_COMPRA.crearOrdenCompra", [p_neto, p_id_pedido, p_vigencia, salida])

    res = salida.getvalue()

    if res == 1:
        messages.success(request, "¡Orden de Compra generada exitosamente!")
        return redirect('indexPedidosProveedor')
    else:
        messages.error(request, "¡Ha ocurrido un error, favor contactar con administrador!")
        return redirect('indexPedidosProveedor')

@login_required
def indexMesas(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("PKG_MESA.listarMesasDisponibles", [out_cur])

    lista= []
    for fila in out_cur:
        lista.append(fila)

    data = {
        'Mesas': lista
    }
    
    return render(request, 'app/administrador/mesas/indexMesas.html', data)

@login_required
def registroMesas(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("PKG_MESA.listarUbicaciones", [out_cur])

    lista= []
    for fila in out_cur:
        lista.append(fila)
    
    data = {
        'Ubicaciones': lista,
    }

    return render(request, 'app/administrador/mesas/registroMesas.html', data)

@login_required
def crearMesas(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    # out_cur = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)

    nro_mesa = int(request.GET["p_nro_mesa"])
    nro_silla = int(request.GET["p_cant_sillas"])
    id_ubicacion = int(request.GET["p_id_ubi"])
    
    cursor.callproc("PKG_MESA.crearMesa", [nro_mesa, nro_silla, id_ubicacion, salida])
    
    res = salida.getvalue()

    if res == 1:
        messages.success(request, "¡La Mesa ha sido registrado exitosamente!")
        return redirect('indexMesas')
    else:
        messages.error(request, "¡Ha ocurrido un error, favor contactar con administrador!")
        return redirect('indexMesas')

@login_required
def modificarMesas(request, id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    out_cur_two = django_cursor.connection.cursor()

    id_mesa = id

    cursor.callproc("PKG_MESA.buscarMesa", [id_mesa, out_cur])
    
    cursor.callproc("PKG_MESA.listarUbicaciones", [out_cur_two])

    lista= []
    for fila in out_cur:
        lista.append(fila)

    lista_ubicacion = []
    for fila in out_cur_two:
        lista_ubicacion.append(fila)


    data = {
        'Mesas': lista,
        'Ubicaciones': lista_ubicacion
    }

    return render(request, 'app/administrador/mesas/editarMesas.html', data)

@login_required
def editarMesas(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    # out_cur = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)

    id_mesa = int(request.GET["id"])
    nro_mesa = int(request.GET["p_nro_mesa"])
    cant_sillas = int(request.GET["p_cant_sillas"])
    id_ubic = int(request.GET["p_id_ubi"])

    cursor.callproc("PKG_MESA.modificarMesa", [id_mesa, nro_mesa, cant_sillas, id_ubic, salida])
    
    res = salida.getvalue()

    if res == 1:
        messages.success(request, "¡La Mesa ha sido editada exitosamente!")
        return redirect('indexMesas')
    else:
        messages.error(request, "¡Ha ocurrido un error, favor contactar con administrador!")
        return redirect('indexMesas')

@login_required
def eliminarMesas(request, id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    # out_cur = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)

    id_mesa = int(id)

    cursor.callproc("PKG_MESA.eliminarMesa", [id_mesa, salida])
    
    messages.success(request, "¡La Mesa ha sido eliminada exitosamente!")
    return redirect(to="indexMesas")

@login_required
def indexGestionCajas(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("PKG_CAJA.listarCajasActivas", [out_cur])

    lista= []
    for fila in out_cur:
        lista.append(fila)

    data = {
        'Cajas': lista
    }
     
    return render(request, 'app/administrador/gestion-cajas/indexCajas.html', data)

@login_required
def registroGestionCajas(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    id_usr = request.user.id
    salida = cursor.var(cx_Oracle.NUMBER)
    
    cursor.callproc("PKG_CAJA.crearCaja", [id_usr, salida])
    
    res = salida.getvalue()

    if res == 1:
        messages.success(request, "¡La Caja ha sido creada exitosamente!")
        return redirect('indexGestionCajas')
    else:
        messages.error(request, "¡Ha ocurrido un error, favor contactar con administrador!")
        return redirect('indexGestionCajas')

@login_required
def eliminarGestionCajas(request, id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    id_caja = int(id)
    salida = cursor.var(cx_Oracle.NUMBER)

    cursor.callproc("PKG_CAJA.eliminarCaja", [id_caja, salida])

    res = salida.getvalue()

    if res == 1:
        messages.success(request, "¡La Caja ha sido eliminada exitosamente!")
        return redirect(to="indexGestionCajas")    
    else:
        messages.error(request, "¡Ha ocurrido un error, favor contactar con administrador!")
        return redirect(to="indexGestionCajas")


@login_required
def modificarGestionCajas(request, id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    id_caja = id

    cursor.callproc("PKG_USUARIO.listarUsuarios", [out_cur])

    lista= []
    for fila in out_cur:
        lista.append(fila)
     
    data = {
        'id': id_caja,
        'Usuarios': lista
    }

    return render(request, 'app/administrador/gestion-cajas/editarCajas.html', data)

@login_required
def asignarUsuarioCaja(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    id_caja = int(request.GET["id_caja"])
    p_usr = int(request.GET["p_usr"])
    salida = cursor.var(cx_Oracle.NUMBER)
    
    cursor.callproc("PKG_CAJA.cambiarUsuarioCaja", [id_caja, p_usr, salida])
    
    res = salida.getvalue()

    if res == 1:
        messages.success(request, "¡Usuario asignado exitosamente!")
        return redirect('indexGestionCajas')
    else:
        messages.error(request, "¡Ha ocurrido un error, favor contactar con administrador!")
        return redirect('indexGestionCajas')


# BODEGA

@login_required
def indexStockProductos(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("PKG_INVENTARIO.listarInventario", [out_cur])

    lista= []
    for fila in out_cur:
        lista.append(fila)

    data = {
        'StockProductos': lista
    }

    return render(request, 'app/bodega/stock-productos/indexStockProductos.html', data)

@login_required
def editarStockProducto(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)

    p_id_inv = int(request.GET["p_id_inv"])
    p_add_stock = int(request.GET["p_add_stock"])
    p_id_medida = int(request.GET["p_id_medida"])

    cursor.callproc("PKG_INVENTARIO.editarInventario", [p_id_inv, p_add_stock, p_id_medida, salida])
    
    res = salida.getvalue()

    if res == 1:
        messages.success(request, "¡El Insumos ha sido editado exitosamente!")
        return redirect(to='indexStockProductos')
    else:
        messages.error(request, "¡Ha ocurrido un error, favor contactar con administrador!")
        return redirect(to='indexStockProductos')

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
def registroRealizarPedido(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur_two = django_cursor.connection.cursor()
    id_usr = request.user.id
    cursor.callproc("PKG_PROVEEDOR.listarProveedor", [out_cur_two])

    lista_proveedor= []
    for fila in out_cur_two:
        lista_proveedor.append(fila)

    data = {
        'id_usuario': id_usr,
        'Proveedores': lista_proveedor,
    }

    return render(request, 'app/bodega/stock-productos/registroStockProductos.html', data)


@login_required
def crearRealizarPedido(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    out_cur_three = django_cursor.connection.cursor()
    
    salida = cursor.var(cx_Oracle.NUMBER)
    salida_id = cursor.var(cx_Oracle.NUMBER)
    p_id_proveedor = int(request.GET["p_id_proveedor"])
    p_id_usuario = int(request.GET["p_id_usuario"])

    cursor.callproc("PKG_PEDIDO_INSUMO.crearPedidoInsumo", [p_id_proveedor, p_id_usuario, salida, salida_id])
    
    p_id_pedido = int(salida_id.getvalue())  
    res = salida.getvalue()

    cursor.callproc("PKG_INVENTARIO.listarInventario", [out_cur])    
    cursor.callproc("PKG_PEDIDO_INSUMO.listarMarca ", [out_cur_three])

    lista= []
    for fila in out_cur:
        lista.append(fila)

    lista_marca= []
    for fila in out_cur_three:
        lista_marca.append(fila)

    data = {
        'id_pedido': p_id_pedido,
        'Inventarios': lista,
        'Marcas': lista_marca,
    }


    if res == 1:
        messages.success(request, "Seleccione lo que pedira")
        return render(request, 'app/bodega/stock-productos/agregarStockProductos.html', data)
    else:
        messages.error(request, "¡Ha ocurrido un error, favor contactar con administrador!")
        return redirect(to='indexStockProductos')

@login_required
def agregarRealizarPedido(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    p_id_pedido = int(request.GET["p_id_pedido"])
    p_id_insumo = int(request.GET["p_id_insumo"])
    p_cantidad = int(request.GET["p_cantidad"])
    p_medida = request.GET["p_medida"]
    p_id_marca = int(request.GET["p_id_marca"])
    salida = cursor.var(cx_Oracle.NUMBER)

    out_cur = django_cursor.connection.cursor()
    out_cur_three = django_cursor.connection.cursor()
    
    cursor.callproc("PKG_PEDIDO_INSUMO.crearDetallePedido", [p_id_pedido, p_id_insumo, p_cantidad, p_medida, p_id_marca, salida])
    res = salida.getvalue()

    cursor.callproc("PKG_INVENTARIO.listarInventario", [out_cur])    
    cursor.callproc("PKG_PEDIDO_INSUMO.listarMarca ", [out_cur_three])

    lista= []
    for fila in out_cur:
        lista.append(fila)

    lista_marca= []
    for fila in out_cur_three:
        lista_marca.append(fila)

    data = {
        'id_pedido': p_id_pedido,
        'Inventarios': lista,
        'Marcas': lista_marca,
    }

    if res == 1:
        messages.success(request, "¡Insumo Agregado Correctamente al Pedido!")
        return render(request, 'app/bodega/stock-productos/agregarStockProductos.html', data)
    else:
        messages.error(request, "¡Ha ocurrido un error, favor contactar con administrador!")
        return redirect(to='indexStockProductos')

@login_required
def modificarStockProductos(request, id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    out_cur_two = django_cursor.connection.cursor()
    id_inventario = id

    cursor.callproc("PKG_INVENTARIO.buscarInvInsumo", [id_inventario, out_cur])
    cursor.callproc("PKG_INVENTARIO.listarUnidadMedida", [out_cur_two])

    lista= []
    for fila in out_cur:
        lista.append(fila)
    
    lista_medida= []
    for fila in out_cur_two:
        lista_medida.append(fila)

    data = {
        'InvetarioStock': lista,
        'UnidadesMedidas': lista_medida
    }
    print(data)

    return render(request, 'app/bodega/stock-productos/editarStockProductos.html', data)

@login_required
def indexPedidosBodegas(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("PKG_PEDIDO_INSUMO.listarTodoPedidos", [out_cur])

    lista= []
    for fila in out_cur:
        lista.append(fila)

    data = {
        'Pedidos': lista
    }
    
    return render(request, 'app/bodega/pedidos/indexPedidosBodegas.html', data)

@login_required
def detallePedidosBodegas(request, id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    id_pedido = id

    cursor.callproc("PKG_PEDIDO_INSUMO.buscarDetPedido", [id_pedido, out_cur])

    lista= []
    for fila in out_cur:
        lista.append(fila)

    data = {
        'DetallePedidos': lista
    }

    return render(request, 'app/bodega/pedidos/detallePedidosBodegas.html', data)


# FINANZAS

@login_required
def indexGestionCajaFinanzas(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("PKG_CAJA.listarCajasActivas", [out_cur])

    lista= []
    for fila in out_cur:
        lista.append(fila)

    data = {
        'Cajas': lista
    }
     
    return render(request, 'app/finanzas/cajas/indexGestionCajaFinanzas.html', data)

@login_required
def buscarCajasFinanzas(request, id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    id_caja = id

    cursor.callproc("PKG_CAJA.buscarCajasActivas", [id_caja, out_cur])

    lista= []
    for fila in out_cur:
        lista.append(fila)
     
    data = {
        'Cajas': lista
    }

    return render(request, 'app/finanzas/cajas/abrirCajas.html', data)

@login_required
def abrirCajasFinanzas(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)

    id_caja = int(request.GET["id_caja"])
    p_amount = int(request.GET["p_amount"])

    cursor.callproc("PKG_CAJA.abrirCaja", [id_caja, p_amount, salida])
    
    res = salida.getvalue()

    if res == 1:
        messages.success(request, "¡Caja abierta exitosamente!")
        return redirect(to='indexGestionCajaFinanzas')
    else:
        messages.error(request, "¡Ha ocurrido un error, favor contactar con administrador!")
        return redirect(to='indexGestionCajaFinanzas')

@login_required
def detalleCajasFinanzas(request, id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    id_caja = id

    cursor.callproc("PKG_CAJA.buscarCajasActivas", [id_caja, out_cur])

    lista= []
    for fila in out_cur:
        lista.append(fila)
     
    data = {
        'Cajas': lista
    }

    return render(request, 'app/finanzas/cajas/detalleCajas.html', data)

@login_required
def cuadrarCajasFinanzas(request, id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    id_caja = id

    cursor.callproc("PKG_CAJA.listarMotivoDescuadre", [out_cur])

    lista= []
    for fila in out_cur:
        lista.append(fila)
     
    data = {
        'id_caja': id_caja,
        'Motivos': lista
    }

    return render(request, 'app/finanzas/cajas/cuadrarCajas.html', data)

@login_required
def crearCuadraturaCajasFinanzas(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    id_caja = int(request.GET["p_id_caja"])
    p_monto_cuadrado = int(request.GET["p_monto_cuadrado"])
    p_tuvo_descuadre = int(request.GET["p_tuvo_descuadre"])
    p_id_motivo = int(request.GET["p_id_motivo"])
    p_monto_descuadre = int(request.GET["p_monto_descuadre"])
    salida = cursor.var(cx_Oracle.NUMBER)

    cursor.callproc("PKG_CAJA.cuadrarCaja", [id_caja, p_monto_cuadrado, p_tuvo_descuadre, p_id_motivo, p_monto_descuadre, salida])
    
    if salida.getvalue() == 1:
        messages.success(request, "¡Caja Cuadrada exitosamente!")
        return redirect('indexGestionCajaFinanzas')
    else:
        messages.error(request, "¡Ha ocurrido un error, favor contactar con administrador!")
        return redirect('indexGestionCajaFinanzas')

@login_required
def indexGestionFacturas(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("PKG_FACTURA.listarFactura", [out_cur])

    lista= []
    for fila in out_cur:
        lista.append(fila)

    data = {
        'Facturas': lista
    }
     
    return render(request, 'app/finanzas/facturas/indexFacturas.html', data)

@login_required
def crearFactura(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    
    salida = cursor.var(cx_Oracle.NUMBER)

    nro_factura = int(request.GET["p_nro_factura"])
    fec_emision = request.GET["p_fec_emision"]
    formated_fec_emision = datetime.strftime(datetime.strptime(fec_emision, "%Y-%m-%d"), "%Y-%m-%d")
    fec_pago = request.GET["p_fec_pago"]
    formated_fec_pago = datetime.strftime(datetime.strptime(fec_pago, "%Y-%m-%d"), "%Y-%m-%d")
    neto = int(request.GET["p_neto"])
    id_oc = int(request.GET["p_id_oc"])
    id_forma_pago = int(request.GET["p_id_forma_pago"])

    print([formated_fec_emision, formated_fec_pago])
    
    cursor.callproc("PKG_FACTURA.crearFactura", [nro_factura, formated_fec_emision, formated_fec_pago, neto, id_oc, id_forma_pago, salida])
    
    if salida.getvalue() == 1:
        messages.success(request, "¡La Factura ha sido creada exitosamente!")
        return redirect('indexGestionFacturas')
    else:
        messages.error(request, "¡Ha ocurrido un error, favor contactar con administrador!")
        return redirect('indexGestionFacturas')

@login_required
def actualizarFacturas(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)

    id_factura = int(request.GET["p_id_factura"])
    nro_factura = int(request.GET["p_nro_factura"])
    fec_emision = request.GET["p_fec_emision"]
    formated_fec_emision = datetime.strftime(datetime.strptime(fec_emision, "%Y-%m-%d"), "%Y-%m-%d")
    fec_pago = request.GET["p_fec_pago"]
    formated_fec_pago = datetime.strftime(datetime.strptime(fec_pago, "%Y-%m-%d"), "%Y-%m-%d")
    neto = int(request.GET["p_neto"])
    id_oc = int(request.GET["p_id_oc"])
    id_forma_pago = int(request.GET["p_id_forma_pago"])

    cursor.callproc("PKG_FACTURA.modificarFactura", [id_factura, nro_factura, formated_fec_emision, formated_fec_pago, neto, id_oc, id_forma_pago, salida])
    
    if salida.getvalue() == 1:
        messages.success(request, "¡La Factura ha sido editada exitosamente!")
        return redirect('indexGestionFacturas')
    else:
        messages.error(request, "¡Ha ocurrido un error, favor contactar con administrador!")
        return redirect('indexGestionFacturas')

@login_required
def registroFacturas(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()

    out_cur = django_cursor.connection.cursor()
    out_cur_two = django_cursor.connection.cursor()

    cursor.callproc("PKG_FACTURA.listarFormaPago", [out_cur])
    cursor.callproc("PKG_ORDEN_COMPRA.listarOC", [out_cur_two])

    lista_forma_pago = []
    for fila in out_cur:
        lista_forma_pago.append(fila)

    lista_orden_compra = []
    for fila in out_cur_two:
        lista_orden_compra.append(fila)
    
    data = {
        'FormaPago': lista_forma_pago,
        'OrdenCompra': lista_orden_compra,
    }

    return render(request, 'app/finanzas/facturas/registroFacturas.html', data)


@login_required
def modificarGestionFacturas(request, id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    out_cur_two = django_cursor.connection.cursor()
    out_cur_three = django_cursor.connection.cursor()

    id_factura = id

    cursor.callproc("PKG_FACTURA.buscarFactura", [id_factura, out_cur])
    cursor.callproc("PKG_FACTURA.listarFormaPago", [out_cur_two])
    cursor.callproc("PKG_ORDEN_COMPRA.listarOC", [out_cur_three])

    lista= []
    for fila in out_cur:
        lista.append(fila)

    lista_forma_pago = []
    for fila in out_cur_two:
        lista_forma_pago.append(fila)

    lista_orden_compra = []
    for fila in out_cur_three:
        lista_orden_compra.append(fila)

    fecha_emision = datetime.strftime(lista[0][2], "%Y-%m-%d")
    fecha_pago = datetime.strftime(lista[0][3], "%Y-%m-%d")

    data = {
        'Factura': lista,
        'OrdenCompra': lista_orden_compra,
        'FormaPago': lista_forma_pago,
        'FechaEmision': fecha_emision,
        'FechaPago': fecha_pago
    }

    return render(request, 'app/finanzas/facturas/editarFacturas.html', data)

@login_required
def eliminarFacturas(request, id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)

    id_factura = int(id)

    cursor.callproc("PKG_FACTURA.eliminarFactura", [id_factura, salida])
    
    messages.success(request, "¡La Factura ha sido eliminada exitosamente!")
    return redirect(to="indexGestionFacturas")

@login_required
def indexInformes(request):
     
    return render(request, 'app/finanzas/informes/indexInformes.html')

# CAJA
@login_required
def indexPagoEfectivo(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("PKG_MESA.listarMesaOcupada", [out_cur])

    lista= []
    for fila in out_cur:
        lista.append(fila)

    data = {
        'Mesas': lista
    }

    return render(request, 'app/caja/pago-efectivo/indexPagoEfectivo.html', data)

@login_required
def detalleMesasCajas(request, id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    id_mesa = id

    cursor.callproc("PKG_MESA.buscarMesa", [id_mesa, out_cur])

    lista= []
    for fila in out_cur:
        lista.append(fila)

    data = {
        'Mesas': lista
    }

    return render(request, 'app/caja/pago-efectivo/detalleMesasCajas.html', data)

@login_required
def ingresarPagoEfectivo(request, id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    id_mesa = id

    cursor.callproc("PKG_MESA.buscarMesa", [id_mesa, out_cur])

    lista= []
    for fila in out_cur:
        lista.append(fila)

    data = {
        'Mesas': lista,
        'id': id_mesa
    }

    return render(request, 'app/caja/pago-efectivo/ingresarPagoEfectivo.html', data)

# COCINA
@login_required
def indexTablero(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    menu = get_object_or_404(Menu, id_menu=id)

    p_id_menu = menu.id_menu

    cursor.callproc("PKG_MENU.listarDetalleMenu", [p_id_menu, out_cur])

    lista= []
    for fila in out_cur:
        lista.append(fila)

    data = {
        'Menus': lista,
        'id': p_id_menu
    }
     
    return render(request, 'app/cocina/tablero/indexTablero.html', data)

@login_required
def entregarPedido(request, id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)

    id_comanda = id

    cursor.callproc("PKG_ORDEN_COMANDA.entregarPedido", [id_comanda, salida])

    if salida.getvalue() == 1:
        messages.success(request, "¡Estado de la comanda cambiado correctamente!")
        return redirect('indexTablero')
    else:
        messages.error(request, "¡Ha ocurrido un error, favor contactar con administrador!")
        return redirect('indexTablero')


# DASHBOARD


@login_required
def dashboard(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    out_cur_two = django_cursor.connection.cursor()
    out_cur_three = django_cursor.connection.cursor()
    out_cur_four = django_cursor.connection.cursor()

    cursor.callproc("PKG_MESA.listarTodoMesa", [out_cur])
    cursor.callproc("PKG_MESA.listarMesasDisponibles", [out_cur_two])
    cursor.callproc("PKG_MESA.listarMesasReservadas", [out_cur_three])
    cursor.callproc("PKG_MESA.listarMesaOcupada", [out_cur_four])

    lista= []
    for fila in out_cur:
        lista.append(fila)
    
    lista_disponibles= []
    for fila in out_cur_two:
        lista_disponibles.append(fila)

    lista_reservadas= []
    for fila in out_cur_three:
        lista_reservadas.append(fila)
    
    lista_ocupadas= []
    for fila in out_cur_four:
        lista_ocupadas.append(fila)

    data = {
        'mesas_totales': len(lista),
        'mesas_disponibles': len(lista_disponibles),
        'mesas_reservadas': len(lista_reservadas),
        'mesas_ocupadas': len(lista_ocupadas),
    }
     
    return render(request, 'app/dashboard.html', data)

# --------------------------------TABLET CLIENTE --------------------------------
def seleccionarMesa(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur_two = django_cursor.connection.cursor()
    cursor.callproc("PKG_MESA.listarTodoMesa", [out_cur_two])
    listar_mesa = []
    for fila in out_cur_two:
        listar_mesa.append(fila)
    data = {
         'listarTodoMesa': listar_mesa
    }
    return render(request, 'app/cliente/seleccionarMesa.html',data)

def clienteMenu(request, id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    
    cursor.callproc("PKG_PRODUCTO.listarProducto", [out_cur])
    lista_producto = []
    for fila in out_cur:
        lista_producto.append(fila)
    data = {
         'listarProducto': lista_producto,
         'id_orden': id
    }
    return render(request, 'app/cliente/clienteMenu.html', data)

def crearOrden(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    v_id_orden = cursor.var(cx_Oracle.NUMBER)
    id_mesa = request.GET["p_id_mesa"]
    request.session['id_mesa'] = id_mesa
    cursor.callproc("PKG_ORDEN_COMANDA.crearOrdenComida", [id_mesa, salida, v_id_orden])
    variable = v_id_orden.getvalue()
    if salida == 1:
        return redirect('seleccionarMesa')
    else:
        return redirect('clienteMenu', id = int(variable))

def crearDetalleOrden(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    id_producto = int(request.GET.get('p_id_producto'))
    cantidad = int(request.GET.get('p_cantidad'))
    id_orden = int(request.GET.get('p_id_orden'))
    cursor.callproc("PKG_ORDEN_COMANDA.crearDetOrdenComida", [id_producto, cantidad, id_orden, salida])
    if salida == 1:
        return redirect('clienteMenu')
    else:
        messages.success(request, "¡producto agregado!")
        return redirect('clienteMenu',id = id_orden)



def listarDetalleOrden(request, id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    p_id_orden = id
    cursor.callproc("PKG_ORDEN_COMANDA.listarDetalleOrden", [p_id_orden, out_cur])
    listar_Detalle_Orden= []
    total = 0

    for fila in out_cur:
        listar_Detalle_Orden.append(fila)
        total += fila[5]
    data = {
         'listarDetalleOrden': listar_Detalle_Orden,
         'id_orden': p_id_orden,
         'total' : total
    }
    print('listar detalle', data)
    return render(request, 'app/cliente/detalleCliente.html', data)

def pagoCliente(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    p_id_mesa = request.session['id_mesa'] 
    cursor.callproc("PKG_PAGOS.solicitarPagoEfectivo", [p_id_mesa, salida])

    if salida == 1:
        return redirect('clienteMenu')
    else:
        del request.session['id_mesa'] 
        messages.success(request, "¡Se le realizara el cobro!")
        return redirect('seleccionarMesa')
    

# ----------------------------------------RESERVA CLIENTE--------------------------------
def reservaCliente(request):
    data = {
        'form': CrearReservaForm()
    }

    if request.method == 'POST':
        formulario = CrearReservaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Reserva exitosa!")
            return redirect()
        data['form'] = formulario
        
    return render(request, 'app/cliente/reservaCliente.html', data)

def principal(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur_two = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    cursor.callproc("PKG_RESERVA.listarDisponibilidad", [out_cur_two])
    cursor.callproc("PKG_MESA.listarMesasDisponibles", [out_cur])

    lista_disponibilidad = []
    for fila in out_cur_two:
        lista_disponibilidad.append(fila)

    listar_Mesas_Disponibles = []
    for fila in out_cur:
        listar_Mesas_Disponibles.append(fila)

    data = {
         'listarDisponibilidad': lista_disponibilidad,
         'listarMesasDisponibles': listar_Mesas_Disponibles
    }
    return render(request, 'app/cliente/principal.html', data)


def CrearReserva(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)

    fecha_reserva = request.GET["p_fecha_reserva"]
    hora_reserva = str(request.GET["p_hora_reserva"])
    asistentes = int(request.GET["p_asistentes"])
    id_mesa = int(request.GET["p_id_mesa"])
    id_disp = int(request.GET["p_id_disp"])
    rut = request.GET["p_rut"]
    nombre = request.GET["p_nombre"]
    telefono = request.GET["p_telefono"]
    correo = request.GET["p_correo"]
    cursor.callproc("PKG_RESERVA.crearReserva", [fecha_reserva, hora_reserva, asistentes, id_mesa, id_disp, rut, nombre, telefono, correo, salida])

    if salida == 1:
        return redirect('principal')
    else:
        messages.success(request, "¡Reserva registrada exitosamente!")
        return redirect('principal')


def buscarReservaRut(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    p_rut = request.GET['p_rut']
    cursor.callproc("PKG_RESERVA.buscarReservaRut", [p_rut, out_cur])

    buscar_Reserva_Rut= []
    for fila in out_cur:
        buscar_Reserva_Rut.append(fila)

    data = {
         'buscarReservaRut': buscar_Reserva_Rut,
    }

    return render(request, 'app/cliente/detalleReserva.html', data)

def eliminarReserva(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    p_id_reserva = request.GET['p_id_reserva']
    # p_id_reserva = int(id)

    cursor.callproc("PKG_RESERVA.eliminarReserva", [p_id_reserva, salida])
    
    messages.success(request, "¡Reserva eliminada exitosamente!")
    return redirect(to="principal")



 




    