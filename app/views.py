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
    
    if salida == 1:
        # ACA ES EL MENSAJE DE ERROR
        return redirect('indexMenus')
    else:
        messages.success(request, "¡El Menu ha sido editado exitosamente!")
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

    if salida == 1:
        # ACA ES EL MENSAJE DE ERROR
        return redirect('indexMenusProductos', id = str(p_id_menu))
    else:
        messages.success(request, "¡El detalle del menu ha sido registrado exitosamente!")
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
    
    if salida == 1:
        # ACA ES EL MENSAJE DE ERROR
        return redirect('indexMenusProductos', id = p_id_menu)
    else:
        messages.success(request, "¡El detalle del menu ha sido editado exitosamente!")
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

    if salida == 1:
        # ACA ES EL MENSAJE DE ERROR
        return redirect('indexProductos')
    else:
        messages.success(request, "¡El producto ha sido registrado exitosamente!")
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
    
    if salida == 1:
        # ACA ES EL MENSAJE DE ERROR
        return redirect('indexProductos')
    else:
        messages.success(request, "¡El Producto ha sido editado exitosamente!")
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
    print(data)
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

def autorizarPedidosProveedor(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    # out_cur = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)

    p_id_pedido = int(request.GET["p_id_pedido"])
    p_opcion1 = int(request.GET["p_opcion1"])
    p_opcion2 = int(request.GET["p_opcion2"])

    cursor.callproc("PKG_PEDIDO_INSUMO.autorizarPedidos", [p_id_pedido, p_opcion1, p_opcion2, salida])
    
    if salida == 1:
        # ACA ES EL MENSAJE DE ERROR
        return redirect('indexPedidosProveedor')
    else:
        messages.success(request, "¡Cambio realizado con exito!")
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


def crearMesas(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    # out_cur = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)

    nro_mesa = int(request.GET["p_nro_mesa"])
    nro_silla = int(request.GET["p_cant_sillas"])
    id_ubicacion = int(request.GET["p_id_ubi"])
    
    cursor.callproc("PKG_MESA.crearMesa", [nro_mesa, nro_silla, id_ubicacion, salida])
    
    if salida == 1:
        # ACA ES EL MENSAJE DE ERROR
        return redirect('indexMesas')
    else:
        messages.success(request, "¡La Mesa ha sido registrado exitosamente!")
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
    
    if salida == 1:
        # ACA ES EL MENSAJE DE ERROR
        return redirect('indexMesas')
    else:
        messages.success(request, "¡La Mesa ha sido editada exitosamente!")
        return redirect('indexMesas')

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

# RESERVA CLIENTE
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

#PRINCIPAL
def principal(request):
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

    return render(request, 'app/cliente/principal.html', data)




    