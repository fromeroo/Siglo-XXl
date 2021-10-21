from django.urls import path
from .views import indexUser, index, indexProveedores, registroProveedores, modificarProveedores, eliminarProveedores, indexMenus, \
    indexInsumos, indexRecetas, indexPedidosProveedor, indexStockProductos, indexGestionCajaFinanzas, indexGestionCajas, \
    indexGestionFacturas,indexInformes, indexPagoEfectivo ,indexMesas, crearMesas, eliminarMesas, editarMesas, indexTablero, modificar_usuario, \
    administrador, dashboard, registro, eliminar_usuario, registroInsumos, modificarInsumos, indexProductos, registroProductos, registroRecetas, \
    modificarRecetas, registroMenus, modificarMenus, crearMenus, eliminarMenus, registroMenusProductos, registroGestionCajas, modificarGestionCajas, registroMesas, modificarMesas, \
    registroStockProductos, modificarStockProductos, registroGestionFacturas, modificarGestionFacturas, clienteMenu, detalleCliente, pagoCliente, crearProveedor, actualizarProveedores, editarMenus, \
    crearInsumo, actualizarInsumos, eliminarInsumos
# APIS
from api import views as api_views

urlpatterns = [
    path('', index, name="index"),
    path('administrador/', administrador, name="administrador"),

    path('administracion/usuario/registro/', registro, name="registro"),
    path('administracion/usuario/', indexUser, name="indexUser"),
    path('administracion/usuario/eliminar/<id>/', eliminar_usuario, name='eliminar_usuario'),
    path('administracion/usuario/modificar/<id>/', modificar_usuario, name='modificar_usuario'),

    path('administracion/proveedores/', indexProveedores, name="indexProveedores"),
    path('crear-proveedor/', crearProveedor, name="crearProveedor"),
    path('actualizar-proveedor/', actualizarProveedores, name="actualizarProveedores"),
    path('administracion/proveedores/registro/', registroProveedores, name="registroProveedores"),
    path('administracion/proveedores/modificar/<id>/', modificarProveedores, name="modificarProveedores"),
    path('administracion/proveedores/eliminar/<id>/', eliminarProveedores, name="eliminarProveedores"),

    path('administracion/menus/', indexMenus, name="indexMenus"),
    path('crear-menus/', crearMenus, name="crearMenus"),
    path('editar-menus/', editarMenus, name="editarMenus"),
    path('administracion/menus/registro/', registroMenus, name="registroMenus"),
    path('administracion/menus/modificar/<id>/', modificarMenus, name="modificarMenus"),
    path('administracion/menus/eliminar/<id>/', eliminarMenus, name="eliminarMenus"),
    path('administracion/menus/registro-producto/<id>/', registroMenusProductos, name="registroMenusProductos"),


    path('administracion/insumos/', indexInsumos, name="indexInsumos"),
    path('crear-insumo/', crearInsumo, name="crearInsumo"),
    path('actualizar-insumo/', actualizarInsumos, name="actualizarInsumos"),
    path('administracion/insumos/registro/', registroInsumos, name="registroInsumos"),
    path('administracion/insumos/modificar/<id>/', modificarInsumos, name="modificarInsumos"),
    path('administracion/insumos/eliminar/<id>/', eliminarInsumos, name="eliminarInsumos"),

    path('administracion/productos/', indexProductos, name="indexProductos"),
    path('administracion/productos/registro/', registroProductos, name="registroProductos"),

    path('administracion/mesas/', indexMesas, name="indexMesas"),
    path('crear-mesas/', crearMesas, name="crearMesas"),
    path('editar-mesas/', editarMesas, name="editarMesas"),
    path('administracion/mesas/eliminar/<id>/', eliminarMesas, name="eliminarMesas"),
    path('administracion/mesas/registro/', registroMesas, name="registroMesas"),
    path('administracion/mesas/modificar/<id>/', modificarMesas, name="modificarMesas"),
    
    path('administracion/recetas/', indexRecetas, name="indexRecetas"),
    path('administracion/recetas/registro/', registroRecetas, name="registroRecetas"),
    path('administracion/recetas/modificar/<id>/', modificarRecetas, name="modificarRecetas"),

    path('administracion/pedidos-proveedor/', indexPedidosProveedor, name="indexPedidosProveedor"),

    path('administracion/menus/', indexMenus, name="indexMenus"),

    path('administracion/gestion-cajas/', indexGestionCajas, name="indexGestionCajas"),
    
    path('administracion/gestion-cajas/registro/', registroGestionCajas, name="registroGestionCajas"),
    
    path('administracion/gestion-cajas/modificar/<id>/', modificarGestionCajas, name="modificarGestionCajas"),

    path('bodega/stock-productos/', indexStockProductos, name="indexStockProductos"),
    path('bodega/stock-productos/registro/', registroStockProductos, name="registroStockProductos"),
    path('bodega/stock-productos/modificar/<id>/', modificarStockProductos, name="modificarStockProductos"),


    path('finanzas/gestion-caja/', indexGestionCajaFinanzas, name="indexGestionCajaFinanzas"),

    path('finanzas/gestion-facturas/', indexGestionFacturas, name="indexGestionFacturas"),
    path('finanzas/gestion-facturas/registro/', registroGestionFacturas, name="registroGestionFacturas"),
    path('finanzas/gestion-facturas/modificar/<id>/', modificarGestionFacturas, name="modificarGestionFacturas"),

    path('finanzas/informes/', indexInformes, name="indexInformes"),

    path('caja/pago-efectivo/', indexPagoEfectivo, name="indexPagoEfectivo"),

    path('cocina/tablero/', indexTablero, name="indexTablero"),

    path('dashboard/', dashboard, name="dashboard"),

    #TABLET CLIENTE
    path('cliente/clienteMenu/', clienteMenu, name="clienteMenu"),
    path('cliente/detalleCliente/', detalleCliente, name="detalleCliente"),
    path('cliente/pagoCliente/', pagoCliente, name="pagoCliente"),

    # APIS URL MESAS
    
    path('api/listar-todo-mesas/', api_views.ListarTodoMesasAPIView.as_view() , name="todoMesas"),
    
    path('api/listar-mesas-disponibles/', api_views.ListarMesasDisponiblesAPIView.as_view() , name="mesasDisponibles"),
    
    path('api/listar-mesas-reservadas/', api_views.ListarMesasReservadasAPIView.as_view() , name="mesasReservadas"),
    
    path('api/listar-mesas-ocupadas/', api_views.ListarMesasOcupadasAPIView.as_view() , name="mesasOcupadas"),
    
    path('api/listar-ubicaciones/', api_views.ListarUbicacionesAPIView.as_view() , name="listarUbicaciones"),
    
    path('api/buscar-mesa/', api_views.BuscarMesaAPIView.as_view() , name="buscarMesa"),

    path('api/buscar-mesa-reserva/', api_views.BuscarMesaReservaAPIView.as_view() , name="buscarMesaReserva"),
    
    path('api/modificar-mesa/', api_views.ModificarMesaAPIView.as_view() , name="modificarMesa"),
    
    path('api/eliminar-mesa/', api_views.EliminarMesaAPIView.as_view() , name="eliminarMesa"),

]
