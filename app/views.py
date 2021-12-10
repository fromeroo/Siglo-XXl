import types
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, View

from app.utils import render_to_pdf
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
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings

@login_required #Etiqueta para que solo pueda ingresar a la def si esta logeado
# Obtiene lista de usuarios mediante models.py
def indexUser(request):
    usuarios = User.objects.all()
    data = {
        'Usuarios': usuarios
    }
    return render(request, 'app/administrador/usuarios/indexUser.html', data)

# Lista los roles de usuario mediante procedimientos almacenados
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

# Cambia el rol de usuario utilizando el procedure actualizarUserGroup
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
# Renderea la vista de usuarios para el administrador
def administrador(request):
    usuario = Usuario.objects.all()
    data = {
        'Usuario': usuario
    }
    return render(request, 'app/administrador.html', data)

@login_required
# Permite a la registrar al usuario enviando una peticion post
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
# Obtiene el id por parametro y modifica el usuario por metodo POST
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
# Permite eliminar el usuario utilizando la funcion DELETE de Django
def eliminar_usuario(request, id):
    usuario = get_object_or_404(User, id=id)
    usuario.delete()
    messages.success(request, "¡El usuario ha sido desactivado exitosamente!")
    return redirect(to="indexUser")

@login_required
# Renderea la vista de proveedores y ejecuta el procedure listaProveedor para poblarla
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
# Renderea el formulario de registro de proveedores poblando los datos para crearlo
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
# Permite crear al proveedor con el procedure crearProveedores al cual le entregan parametros GET
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
    if request.GET["p_nro_casa"]:
        numero_casa = int(request.GET["p_nro_casa"])
    else: 
        numero_casa = ''
    tipo_direccion = int(request.GET["p_tipo_dir"])
    id_comuna= int(request.GET["p_id_com"])
    
    cursor.callproc("PKG_PROVEEDOR.crearProveedores", [rut, dv, razon_social, nombre_corto, telefono, correo, id_giro, direccion, numero_dirrecion, numero_casa, tipo_direccion, id_comuna, salida])
    
    if salida.getvalue() == 1:
        messages.success(request, "¡El Proveedor ha sido registrado exitosamente!")
        return redirect('indexProveedores')
    else:
        messages.error(request, "¡Ha ocurrido un error, favor contactar con administrador!")
        return redirect('indexProveedores')

@login_required
# Permite modificar al proveedor con el procedure modificarProveedores al cual le entregan parametros GET
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
    if request.GET["p_nro_casa"]:
        numero_casa = int(request.GET["p_nro_casa"])
    else: 
        numero_casa = ''
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
# Envia al formulario de proveedores con los datos precargados para su modificacion
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
# Permite eliminar el proveedor pasando el id al procedure eliminarProveedor
def eliminarProveedores(request, id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    # out_cur = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)

    id_proveedor = int(id)

    cursor.callproc("PKG_PROVEEDOR.eliminarProveedor", [id_proveedor, salida])
    
    messages.success(request, "¡El proveedor ha sido eliminado exitosamente!")
    return redirect(to="indexProveedores")

# +++++++ NOMENCLATURAS -> ********** ++++++++
# INDEX********* -> renderea la pagina principal de la nomenclatura
# REGISTER********* -> renderea el formulario de registro de la nomenclatura
# CREAR********* -> crea la nomenclatura con el procedure crearNomenclatura
# MODIFICAR********* -> rendera el formulario para modificar la nomenclatura
# ACTUALIZAR********* -> actualiza la nomenclatura con el procedure actualizarNomenclatura
# ELIMINAR********* -> elimina la nomenclatura con el procedure eliminarNomenclatura



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
    #out_cur_two = django_cursor.connection.cursor()

    cursor.callproc("PKG_INSUMO.listarTipoInsumo", [out_cur])
    #cursor.callproc("PKG_INSUMO.listarCategoriaInsumo", [out_cur_two])

    lista_tipo_insumo= []
    for fila in out_cur:
        lista_tipo_insumo.append(fila)

    

    data = {
        'TipoInsumos': lista_tipo_insumo,
    }
     
    return render(request, 'app/administrador/insumos/registroInsumos.html', data)

@login_required
def crearInsumo(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)

    nombre_insumo = request.GET["p_nom_insumo"]
    tipo_insumo = int(request.GET["p_id_tipo_insumo"])
    #categoria_insumo = int(request.GET["p_id_cat_insumo"])

    cursor.callproc("PKG_INSUMO.crearInsumo", [nombre_insumo, tipo_insumo,  salida])
    
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

    salida = cursor.var(cx_Oracle.NUMBER)

    cursor.callproc("PKG_INSUMO.modificarInsumo", [id_insumo, nombre_insumo, tipo_insumo, salida])
    
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
    #out_cur_three = django_cursor.connection.cursor()
    id_insumo = id

    cursor.callproc("PKG_INSUMO.buscarInsumo", [id_insumo, out_cur])
    cursor.callproc("PKG_INSUMO.listarTipoInsumo", [out_cur_two])
    #cursor.callproc("PKG_INSUMO.listarCategoriaInsumo", [out_cur_three])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    lista_tipo_insumo = []
    for fila in out_cur_two:
        lista_tipo_insumo.append(fila)

    

    data = {
        'Insumo': lista,
        'TipoInsumo': lista_tipo_insumo,
        #'CategoriaInsumo': lista_categoria_insumo
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
    link_imagen = request.GET["link_imagen"]

    cursor.callproc("PKG_PRODUCTO.crearProducto", [p_nom_producto, p_precio, p_id_cat, p_id_tipo, p_id_receta, link_imagen, salida])

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
    link_imagen = request.GET["link_imagen"]

    cursor.callproc("PKG_PRODUCTO.modificarProducto", [p_id_producto, p_nom_prod, p_precio, p_id_cat, p_id_tipo, p_id_receta, link_imagen, salida])
    
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
def indexRecetasTwo(request):
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
     
    return render(request, 'app/administrador/recetas/indexRecetasTwo.html', data)

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
def indexIngredientesRecetasTwo(request, id):
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

    return render(request, 'app/administrador/recetas/indexIngredientesRecetasTwo.html', data)

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
def modificarIngredientesRecetas(request, id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    out_cur_two = django_cursor.connection.cursor()

    id_receta = id

    cursor.callproc("PKG_RECETA.buscarIngrediente", [id_receta, out_cur])
    
    cursor.callproc("PKG_INSUMO.listarInsumo", [out_cur_two])

    lista= []
    for fila in out_cur:
        lista.append(fila)

    lista_insumo = []
    for fila in out_cur_two:
        lista_insumo.append(fila)

    data = {
        'Ingredientes': lista,
        'Insumos': lista_insumo,
        'id': id_receta
    }

    return render(request, 'app/administrador/recetas/editarIngredientes.html', data)
    
@login_required
def editarIngredientesRecetas(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    salida_id_receta = cursor.var(cx_Oracle.NUMBER)

    p_id_receta = int(request.GET["p_id_receta"])
    p_cantidad_nueva = int(request.GET["p_cantidad_nueva"])

    cursor.callproc("PKG_RECETA.modificarIngrediente", [p_id_receta, p_cantidad_nueva, salida, salida_id_receta])
    
    res = salida.getvalue()
    res_dos = salida_id_receta.getvalue()

    if res == 1:
        messages.success(request, "¡El Ingrediente ha sido editado exitosamente!")
        return redirect('indexRecetas')
    else:
        messages.error(request, "¡Ha ocurrido un error, favor contactar con administrador!")
        return redirect('indexRecetas')

@login_required
def eliminarIngredientesRecetas(request, id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    salida_dos = cursor.var(cx_Oracle.NUMBER)
    id_receta = id

    cursor.callproc("PKG_RECETA.eliminarIngrediente", [id_receta, salida, salida_dos])
    
    messages.success(request, "¡El Ingrediente ha sido eliminado exitosamente!")
    return redirect(to="indexRecetas")


@login_required
def indexPedidosProveedor(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("PKG_PEDIDO_INSUMO.listarTodoPedidos", [out_cur])

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
    out_cur_two = django_cursor.connection.cursor()
    id_pedido = id

    cursor.callproc("PKG_PEDIDO_INSUMO.buscarDetPedido", [id_pedido, out_cur])
    cursor.callproc("PKG_PEDIDO_INSUMO.buscarPedido", [id_pedido, out_cur_two])

    lista= []
    for fila in out_cur:
        lista.append(fila)

    lista_pedido= []
    for fila in out_cur_two:
        lista_pedido.append(fila)

    data = {
        'DetallePedidos': lista,
        'Pedido': lista_pedido
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
    elif res == 2:
        messages.error(request, "¡El Numero de mesa ingresado ya existe!")
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
def indexDisponibilidades(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("PKG_RESERVA.listarDisponibilidad", [out_cur])

    lista= []
    for fila in out_cur:
        lista.append(fila)

    data = {
        'Disponibilidades': lista
    }

    return render(request, 'app/administrador/disponibilidad/indexDisponibilidad.html', data)

@login_required
def registroDisponibilidades(request):
    
    return render(request, 'app/administrador/disponibilidad/registroDisponibilidad.html')

@login_required
def crearDisponibilidades(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    # out_cur = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)

    p_fec_disp = request.GET["p_fec_disp"]
    formated_fec_disp = datetime.strftime(datetime.strptime(p_fec_disp, "%Y-%m-%d"), "%Y-%m-%d")
    p_hora_disp = request.GET["p_hora_disp"]
    formated_hora_disp = datetime.strftime(datetime.strptime(p_hora_disp, "%H:%M"),"%H:%M")
    p_personas = int(request.GET["p_personas"])
    
    cursor.callproc("PKG_RESERVA.crearDisponibilidad", [formated_fec_disp, formated_hora_disp, p_personas, salida])
    
    res = salida.getvalue()

    if res == 1:
        messages.success(request, "¡La Disponibilidad ha sido registrado exitosamente!")
        return redirect('indexDisponibilidades')
    else:
        messages.error(request, "¡Ha ocurrido un error, favor contactar con administrador!")
        return redirect('indexDisponibilidades')

@login_required
def modificarDisponibilidades(request, id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    id_disponibilidad = id

    cursor.callproc("PKG_RESERVA.buscarDisponibilidad", [id_disponibilidad, out_cur])

    lista= []
    for fila in out_cur:
        lista.append(fila)

    fecha = datetime.strftime(lista[0][3], "%Y-%m-%d")

    data = {
        'Disponibilidades': lista,
        'fecha': fecha
    }

    return render(request, 'app/administrador/disponibilidad/editarDisponibilidad.html', data)

@login_required
def editarDisponibilidades(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    # out_cur = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)

    id_disponibilidad = int(request.GET["id"])
    p_fec_disp = request.GET["p_fec_disp"]
    formated_fec_disp = datetime.strftime(datetime.strptime(p_fec_disp, "%Y-%m-%d"), "%Y-%m-%d")
    p_hora_disp = request.GET["p_hora_disp"]
    formated_hora_disp = datetime.strftime(datetime.strptime(p_hora_disp, "%H:%M"),"%H:%M")
    p_personas = int(request.GET["p_personas"])

    cursor.callproc("PKG_RESERVA.modificarDisponibilidad", [id_disponibilidad, formated_fec_disp, formated_hora_disp, p_personas, salida])
    
    res = salida.getvalue()

    if res == 1:
        messages.success(request, "¡La Disponibilidad ha sido editada exitosamente!")
        return redirect('indexDisponibilidades')
    else:
        messages.error(request, "¡Ha ocurrido un error, favor contactar con administrador!")
        return redirect('indexDisponibilidades')

@login_required
def eliminarDisponibilidades(request, id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    # out_cur = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)

    id_disponibilidad = int(id)

    cursor.callproc("PKG_RESERVA.eliminarDisponibilidad", [id_disponibilidad, salida])
    
    messages.success(request, "¡La Disponibilidad ha sido eliminada exitosamente!")
    return redirect(to="indexDisponibilidades")

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
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("PKG_USUARIO.listarUsuarios", [out_cur])

    lista= []
    for fila in out_cur:
        lista.append(fila)
     
    data = {
        'Usuarios': lista,
    }

    return render(request, 'app/administrador/gestion-cajas/registroCajas.html', data)

@login_required
def crearGestionCajas(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    id_usr = int(request.GET["p_usr"])
    salida = cursor.var(cx_Oracle.NUMBER)
    
    cursor.callproc("PKG_CAJA.crearCaja", [id_usr, salida])
    
    res = salida.getvalue()

    if res == 1:
        messages.success(request, "¡La Caja ha sido creada exitosamente!")
        return redirect('indexGestionCajas')
    elif res == 2:
        messages.error(request, "¡Usuario ya tiene una caja asignada!")
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
    out_cur_four = django_cursor.connection.cursor()
    
    salida = cursor.var(cx_Oracle.NUMBER)
    salida_id = cursor.var(cx_Oracle.NUMBER)
    p_id_proveedor = int(request.GET["p_id_proveedor"])
    p_id_usuario = int(request.GET["p_id_usuario"])

    cursor.callproc("PKG_PEDIDO_INSUMO.crearPedidoInsumo", [p_id_proveedor, p_id_usuario, salida, salida_id])
    
    p_id_pedido = int(salida_id.getvalue())  
    res = salida.getvalue()

    cursor.callproc("PKG_INVENTARIO.listarInventario", [out_cur])    
    cursor.callproc("PKG_PEDIDO_INSUMO.listarMarca ", [out_cur_three])

    cursor.callproc("PKG_PEDIDO_INSUMO.buscarDetPedido", [p_id_pedido, out_cur_four])

    lista= []
    for fila in out_cur:
        lista.append(fila)

    lista_marca= []
    for fila in out_cur_three:
        lista_marca.append(fila)

    lista_detalle_pedido= []
    for fila in out_cur_four:
        lista_detalle_pedido.append(fila)

    data = {
        'id_pedido': p_id_pedido,
        'Inventarios': lista,
        'Marcas': lista_marca,
        'DetallePedido': lista_detalle_pedido,
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
    out_cur_four = django_cursor.connection.cursor()
    
    cursor.callproc("PKG_PEDIDO_INSUMO.crearDetallePedido", [p_id_pedido, p_id_insumo, p_cantidad, p_medida, p_id_marca, salida])
    res = salida.getvalue()

    cursor.callproc("PKG_INVENTARIO.listarInventario", [out_cur])    
    cursor.callproc("PKG_PEDIDO_INSUMO.listarMarca ", [out_cur_three])
    cursor.callproc("PKG_PEDIDO_INSUMO.buscarDetPedido", [p_id_pedido, out_cur_four])

    lista= []
    for fila in out_cur:
        lista.append(fila)

    lista_marca= []
    for fila in out_cur_three:
        lista_marca.append(fila)

    lista_detalle_pedido= []
    for fila in out_cur_four:
        lista_detalle_pedido.append(fila)

    data = {
        'id_pedido': p_id_pedido,
        'Inventarios': lista,
        'Marcas': lista_marca,
        'DetallePedido': lista_detalle_pedido,
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
def indexAperturaCajasFinanzas(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("PKG_CAJA.listarCajasSinApertura", [out_cur])

    lista= []
    for fila in out_cur:
        lista.append(fila)

    data = {
        'Cajas': lista
    }
     
    return render(request, 'app/finanzas/cajas/indexAperturaCajasFinanzas.html', data)

@login_required
def indexGestionCajaFinanzas(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("PKG_CAJA.listarAperturasCaja", [out_cur])

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
def detalleCajasFinanzasAperturas(request, id):
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

    return render(request, 'app/finanzas/cajas/detalleCajasAperturas.html', data)

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
def verGestionFactura(request, id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    id_factura = id

    cursor.callproc("PKG_FACTURA.buscarFactura", [id_factura, out_cur])

    lista= []
    for fila in out_cur:
        lista.append(fila)

    data = {
        'Factura': lista
    }

    return render(request, 'app/finanzas/facturas/verFacturas.html', data)


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

    cursor.callproc("PKG_PAGOS.listarMesaPagoEfectivo", [out_cur])

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

    cursor.callproc("PKG_PAGOS.buscarMesaEfectivo", [id_mesa, out_cur])

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
    out_cur_two = django_cursor.connection.cursor()

    id_mesa = id

    cursor.callproc("PKG_PAGOS.buscarMesaEfectivo", [id_mesa, out_cur])
    cursor.callproc("PKG_CAJA.listarAperturasCaja", [out_cur_two])

    lista= []
    for fila in out_cur:
        lista.append(fila)

    lista_caja= []
    for fila in out_cur_two:
        lista_caja.append(fila)

    data = {
        'Mesas': lista,
        'id': id_mesa,
        'Cajas': lista_caja
    }
    

    return render(request, 'app/caja/pago-efectivo/ingresarPagoEfectivo.html', data)


@login_required
def crearIngresarPagoEfectivo(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    # out_cur = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    salida_venta = cursor.var(cx_Oracle.NUMBER)
    salida_monto = cursor.var(cx_Oracle.NUMBER)
    salida_dos = cursor.var(cx_Oracle.NUMBER)
    salida_id_boleta = cursor.var(cx_Oracle.NUMBER)

    p_id_mesa = int(request.GET["p_id_mesa"])
    p_id_orden = int(request.GET["p_id_orden"])
    p_monto_venta = int(request.GET["p_monto_venta"])
    p_monto2 = int(request.GET["p_monto2"])
    p_id_caja = int(request.GET["p_id_caja"])
    
    cursor.callproc("PKG_PAGOS.ingresarPagoEfectivo", [p_id_mesa, p_id_orden, p_monto_venta, p_monto2, p_id_caja, salida, salida_venta, salida_monto])
    
    res = salida.getvalue()
    res_salida_venta = salida_venta.getvalue()



    if res == 1:
        cursor.callproc("PKG_PAGOS.generarBoleta", [p_monto2, res_salida_venta, salida_dos, salida_id_boleta])
        
        res_salida_dos = salida_dos.getvalue()
        res_salida_id_boleta = salida_id_boleta.getvalue()

        data = {
            'id_boleta': int(res_salida_id_boleta), 
        }

        if res_salida_dos == 1:
            messages.success(request, "¡Pago en Efectivo realizado exitosamente!")
            return render(request, 'app/caja/pago-efectivo/generarBoleta.html', data)
        else:
            messages.error(request, "¡Error al generar la boleta!")
            return redirect('indexPagoEfectivo')

    elif res == 2:
        messages.error(request, "¡El valor ingresado es mayor al monto a pagar!")
        return redirect('indexPagoEfectivo')
    else:
        messages.error(request, "¡Ha ocurrido un error, favor contactar con administrador!")
        return redirect('indexPagoEfectivo')

def imprimirBoleta(request, id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    id_boleta = id

    cursor.callproc("PKG_PAGOS.imprimirBoleta", [id_boleta, out_cur])

    lista= []
    for fila in out_cur:
        lista.append(fila)

    print(lista[0])

    data = {
        'boletas': lista[0],
    }

    pdf = render_to_pdf('app/caja/informes/boletaEfectivo.html', data)

    return HttpResponse(pdf, content_type='application/pdf')


# COCINA
@login_required
def indexTablero(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    out_cur_two = django_cursor.connection.cursor()

    cursor.callproc("PKG_ORDEN_COMANDA.listarComandaNueva", [out_cur])
    cursor.callproc("PKG_ORDEN_COMANDA.listarEstadoComanda", [out_cur_two])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    lista_two = []
    for fila in out_cur_two:
        lista_two.append(fila)

    data = {
        'OrdenComanda': lista,
        'EstadoComanda': lista_two
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

@login_required
def prepararComanda(request, id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)

    id_comanda = id

    cursor.callproc("PKG_ORDEN_COMANDA.prepararComanda", [id_comanda, salida])

    if salida.getvalue() == 1:
        messages.success(request, "¡Estado de la comanda cambiado correctamente!")
        return redirect('indexTablero')
    else:
        messages.error(request, "¡Ha ocurrido un error, favor contactar con administrador!")
        return redirect('indexTablero')

@login_required
def detalleComanda(request, id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    id_comanda = id

    cursor.callproc("PKG_ORDEN_COMANDA.verDetalleComanda", [id_comanda, out_cur])

    lista= []
    for fila in out_cur:
        lista.append(fila)

    data = {
        'Comandas': lista
    }

    return render(request, 'app/cocina/tablero/detalleComanda.html', data)

# DASHBOARD


@login_required
def dashboard(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    out_cur_two = django_cursor.connection.cursor()
    out_cur_three = django_cursor.connection.cursor()
    out_cur_four = django_cursor.connection.cursor()
    out_cur_five = django_cursor.connection.cursor()
    out_cur_six = django_cursor.connection.cursor()
    out_cur_seven = django_cursor.connection.cursor()

    cursor.callproc("PKG_MESA.listarTodoMesa", [out_cur])
    cursor.callproc("PKG_MESA.listarMesasDisponibles", [out_cur_two])
    cursor.callproc("PKG_MESA.listarMesasReservadas", [out_cur_three])
    cursor.callproc("PKG_MESA.listarMesaOcupada", [out_cur_four])
    cursor.callproc("PKG_GRAFICOS.mostrarVentaDiaria", [out_cur_five])
    cursor.callproc("PKG_GRAFICOS.mostrarReservasDiarias", [out_cur_six])
    cursor.callproc("PKG_GRAFICOS.mostrarFacturasDiarias", [out_cur_seven])

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

    total_venta_diaria= []
    for fila in out_cur_five:
        total_venta_diaria.append(fila)
    
    total_reserva_diaria= []
    for fila in out_cur_six:
        total_reserva_diaria.append(fila)
    
    total_factura_diaria= []
    for fila in out_cur_seven:
        total_factura_diaria.append(fila)

    data = {
        'mesas_totales': len(lista),
        'mesas_disponibles': len(lista_disponibles),
        'mesas_reservadas': len(lista_reservadas),
        'mesas_ocupadas': len(lista_ocupadas),
        'venta_diaria': total_venta_diaria,
        'reserva_diaria': total_reserva_diaria,
        'factura_diaria': total_factura_diaria,
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
    # ------------------------------------------
    out_cur = django_cursor.connection.cursor()
    out_cur2 = django_cursor.connection.cursor()
    p_id_mesa = request.session['id_mesa']
    cursor.callproc("PKG_PRODUCTO.listarProducto", [out_cur2])
    lista_producto = []
    for fila in out_cur2:
        lista_producto.append(fila)
    # ------------------------------------------
    id_producto = int(request.GET.get('p_id_producto'))
    cantidad = int(request.GET.get('p_cantidad'))
    id_orden = int(request.GET.get('p_id_orden'))
    cursor.callproc("PKG_ORDEN_COMANDA.crearDetOrdenComida", [id_producto, cantidad, id_orden, salida])
    cursor.callproc("PKG_PAGOS.listarDetalleOrdenMesa", [p_id_mesa, out_cur])
    listar_Detalle_Orden= []
    total = 0
    for fila in out_cur:
        listar_Detalle_Orden.append(fila)
        total += fila[2]
    # ------------------------------------------
    data = {
         'listarDetalleOrden': listar_Detalle_Orden,
         'total' : total,
         'id_orden' : id_orden,
         'listarProducto': lista_producto
    } 
    if salida == 1:
        return render(request, 'app/cliente/clienteMenu.html', data)
    else:
        messages.success(request, "¡producto agregado!")
        return render(request, 'app/cliente/clienteMenu.html', data)



def listarDetalleOrden(request, id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    p_id_mesa = request.session['id_mesa']
    p_id_orden = id
    cursor.callproc("PKG_PAGOS.listarDetalleOrdenMesa", [p_id_mesa, out_cur])
    listar_Detalle_Orden= []
    total = 0

    for fila in out_cur:
        listar_Detalle_Orden.append(fila)
        total += fila[2]
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

def ingresarPagotarjeta(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    salida_dos = cursor.var(cx_Oracle.NUMBER)
    salida_tres = cursor.var(cx_Oracle.NUMBER)
    salida_cuatro = cursor.var(cx_Oracle.DATETIME)
    p_id_mesa = int(request.session['id_mesa'])
    p_id_orden = int(request.GET.get('p_id_orden'))
    p_monto_venta = int(request.GET.get('p_monto_venta'))
    p_correo = request.GET.get('p_correo')
    print("id_mesa",p_id_mesa,"id_orden",p_id_orden,"monto_venta",p_monto_venta, "correo", p_correo)
    cursor.callproc("PKG_PAGOS.ingresarPagotarjeta", [p_id_mesa, p_id_orden, p_monto_venta, salida,salida_dos,salida_tres,salida_cuatro])
    salida_boleta = salida_dos.getvalue()
    salida_monto = salida_tres.getvalue()
    salida_fecha = salida_cuatro.getvalue()
    print(salida_boleta,' ',salida_monto,' ',salida_fecha )
    # data = {
    #     'id_boleta': int(salida_boleta),
    #     'monto_boleta':  int(salida_monto),
    #     'fecha_boleta': salida_fecha
    # }
    if salida == 1:
        return redirect('clienteMenu')
    else:
        del request.session['id_mesa'] 
        
        subject = 'Pago Realizado'

        template = render_to_string('email_template_transferencia.html', {
            'numero_boleta': int(salida_boleta),
            'precio': int(salida_monto),
            'fecha': salida_fecha,
        })

        email = EmailMessage(
            subject,
            template,
            settings.EMAIL_HOST_USER,
            [p_correo]
        )
        
        email.fail_silently = False
        email.send()

        messages.success(request, "redirigiendo a webpay")
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
    out_cur = django_cursor.connection.cursor()
    asistentes = int(request.GET["p_asistentes"])
    id_mesa = int(request.GET["p_id_mesa"])
    id_disp = int(request.GET["p_id_disp"])
    cursor.callproc("PKG_RESERVA.buscarDisponibilidad", [id_disp, out_cur])
    
    data= []
    for fila in out_cur:
        data.append(fila)
        
    fecha_reserva = data[0][3]
    hora_reserva = data[0][4]
    rut = request.GET["p_rut"]
    nombre = request.GET["p_nombre"]
    telefono = request.GET["p_telefono"]
    correo = request.GET["p_correo"]
    cursor.callproc("PKG_RESERVA.crearReserva", [fecha_reserva, hora_reserva, asistentes, id_mesa, id_disp, rut, nombre, telefono, correo, salida])

    if salida == 1:
        return redirect('principal')
    else:
        subject = 'Reserva Realizada'

        template = render_to_string('email_template.html', {
            'nombre': nombre,
            'fecha': fecha_reserva,
            'hora': hora_reserva,
            'asistentes': asistentes
        })

        email = EmailMessage(
            subject,
            template,
            settings.EMAIL_HOST_USER,
            [correo]
        )
        
        email.fail_silently = False
        email.send()

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

def eliminarReserva(request, id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    #p_id_reserva = request.GET['p_id_reserva']
    # p_id_reserva = int(id)

    cursor.callproc("PKG_RESERVA.eliminarReserva", [id, salida])
    
    messages.success(request, "¡Reserva eliminada exitosamente!")
    return redirect(to="principal")

class ListaFacturaListView(ListView):
    model = Factura
    template_name = "app/finanzas/informes/facturas.html"    
    context_object_name = 'facturas'

# class ListEmpleadosPdf(View):

#     def get(self, request, *args, **kwargs):
#         facturas = Factura.objects.all().filter()
#         data = {
#             'facturas': facturas
#         }
#         pdf = render_to_pdf('app/finanzas/informes/facturas.html', data)
#         return HttpResponse(pdf, content_type='application/pdf')

class ListFacturasPasadasPdf(View):

    def get(self, request, *args, **kwargs):
        facturas = Factura.objects.all().filter(id_est_factura=1)
        data = {
            'facturas': facturas,
            'estado': 1
        }
        pdf = render_to_pdf('app/finanzas/informes/facturas.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

class ListFacturasPagadasPdf(View):

    def get(self, request, *args, **kwargs):
        facturas = Factura.objects.all().filter(id_est_factura=2)
        data = {
            'facturas': facturas,
            'estado': 2
        }
        pdf = render_to_pdf('app/finanzas/informes/facturas.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

class ListFacturasVencidasPdf(View):

    def get(self, request, *args, **kwargs):
        facturas = Factura.objects.all().filter(id_est_factura=5)
        data = {
            'facturas': facturas,
            'estado': 5
        }
        pdf = render_to_pdf('app/finanzas/informes/facturas.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

class ListFacturaById(View):
    def get(self, request, *args, **kwargs):
        context = Factura.objects.get(id_factura=self.kwargs['id'])
        data = {
            'factura': context,
        }
        
        pdf = render_to_pdf('app/finanzas/informes/listafacturas.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

def indexReporteUtilidad(request):
    return render(request, 'app/finanzas/reporte/utilidad.html')

def descargarReporteUtilidad(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    out_cur_two = django_cursor.connection.cursor()
    salida_one = cursor.var(cx_Oracle.STRING)
    salida_two = cursor.var(cx_Oracle.NUMBER)

    tipo = int(request.GET["tipo"])

    if tipo == 1:
        cursor.callproc("PKG_REPORTES.generarTotalVentaDiaria", [out_cur])

        lista= []
        for fila in out_cur:
            lista.append(fila)

        p_one = int(lista[0][0] if lista[0][0] is not None else 1)

        cursor.callproc("PKG_REPORTES.generarTotalFacturaDiaria", [out_cur_two])

        lista_two= []
        for fila in out_cur_two:
            lista_two.append(fila)

        p_two = int(lista_two[0][0] if lista_two[0][0] is not None else 1)

        print(int(p_one), int(p_two))

        cursor.callproc("PKG_REPORTES.mostrarUtilidadDiaria", [p_one, p_two, salida_one, salida_two])

        utilidad = salida_one.getvalue()

        print(utilidad)


        data = {
            'tipo': 1,
            'titulo': 'Utilidad Diaria',
            'utilidad': utilidad,
            'total_venta_diaria': p_one,
            'total_factura_diaria': p_two,
        }
        
        pdf = render_to_pdf('app/finanzas/reporte/utilidad-mensual-pdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
    else:
        cursor.callproc("PKG_REPORTES.generarTotalVentaMensual", [out_cur])

        lista= []
        for fila in out_cur:
            lista.append(fila)

        p_one = int(lista[0][0] if lista[0][0] is not None else 1)

        cursor.callproc("PKG_REPORTES.generarTotalFacturaMensual", [out_cur_two])

        lista_two= []
        for fila in out_cur_two:
            lista_two.append(fila)

        p_two = int(lista_two[0][0] if lista_two[0][0] is not None else 1)

        print(int(p_one), int(p_two))

        cursor.callproc("PKG_REPORTES.generarUtilidadMensual", [p_one, p_two, salida_one, salida_two])

        utilidad = salida_one.getvalue()

        print(utilidad)

        data = {
            'tipo': 2,
            'titulo': 'Utilidad Mes Actual',
            'utilidad': utilidad,
            'total_venta_mensual': p_one,
            'total_factura_mensual': p_two,
        }
        
        pdf = render_to_pdf('app/finanzas/reporte/utilidad-mensual-pdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
class ListReporteUtilidadDiaria(View):

    def get(self, request, *args, **kwargs):
        
        django_cursor = connection.cursor()
        cursor = django_cursor.connection.cursor()
        out_cur = django_cursor.connection.cursor()
        salida_two = cursor.var(cx_Oracle.NUMBER)
        salida_three = cursor.var(cx_Oracle.NUMBER)

        cursor.callproc("PKG_REPORTES.generarTotalVentaDiaria", [out_cur])

        lista= []
        for fila in out_cur:
            lista.append(fila)

        print(lista)

        data = {
            'salida_one': lista
        }
        
        pdf = render_to_pdf('app/finanzas/reporte/utilidad-mensual-pdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


def generarReporteAdministrador(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    cursor_one = django_cursor.connection.cursor()
    cursor_two = django_cursor.connection.cursor()
    cursor_three = django_cursor.connection.cursor()

    p_fec_disp = request.GET["initial_date"]
    p_fecha_inicial = datetime.strftime(datetime.strptime(p_fec_disp, "%Y-%m-%d"), "%Y-%m-%d")

    p_fec_disp = request.GET["finish_date"]
    p_fecha_final = datetime.strftime(datetime.strptime(p_fec_disp, "%Y-%m-%d"), "%Y-%m-%d")

    cursor.callproc("PKG_REPORTES.informeClientesAtendidos", [p_fecha_inicial, p_fecha_final, cursor_one])    
    cursor.callproc("PKG_REPORTES.informePlatosConsumidos", [p_fecha_inicial, p_fecha_final, cursor_two])    
    cursor.callproc("PKG_REPORTES.tiempoAtencion", [p_fecha_inicial, p_fecha_final, cursor_three])    

    clientes_atendidos = []
    for cliente_atendido in cursor_one:
        clientes_atendidos.append(cliente_atendido)

    platos_consumidos = []
    for plato_consumido in cursor_one:
        platos_consumidos.append(plato_consumido)

    tiempo_atencion = []
    for t_atencion in cursor_one:
        tiempo_atencion.append(t_atencion)

    data = {
        'clientes_atendidos': clientes_atendidos,
        'platos_consumidos': platos_consumidos,
        'tiempo_atencion': platos_consumidos,
    }

    pdf = render_to_pdf('app/administrador/reporte/generarReporte.html', data)
    return HttpResponse(pdf, content_type='application/pdf')

def indexReporteAdministrador(request):
    return render(request, 'app/administrador/reporte/indexReporte.html')