from django.urls import path
from .views import index, administrador, registro, indexUser, eliminar_usuario, modificar_usuario, \
    indexProveedores, crearProveedor, actualizarProveedores, registroProveedores, modificarProveedores, eliminarProveedores, \
    indexMenus, crearMenus, editarMenus, registroMenus, modificarMenus, eliminarMenus, \
    indexMenusProductos, registroMenusProductos, modificarMenusProductos, crearMenusProductos, editarMenusProductos, \
    indexInsumos, crearInsumo, actualizarInsumos, registroInsumos, modificarInsumos, eliminarInsumos, \
    indexProductos, crearProductos, editarProductos, registroProductos, modificarProductos, eliminarProductos, \
    indexMesas, crearMesas, editarMesas, eliminarMesas, registroMesas, modificarMesas, \
    indexRecetas, registroRecetas, modificarRecetas, crearRecetas, editarRecetas, eliminarRecetas, \
    indexIngredientesRecetas, registroIngredientesRecetas, crearIngredientesRecetas,\
    indexPedidosProveedor, detallePedidosProveedor, autorizarPedidosProveedor, \
    indexGestionCajas, registroGestionCajas, modificarGestionCajas, \
    indexStockProductos, registroStockProductos, modificarStockProductos, \
    indexGestionCajaFinanzas, \
    indexGestionFacturas, registroGestionFacturas, modificarGestionFacturas, \
    indexInformes, \
    indexPagoEfectivo, \
    indexTablero, \
    dashboard, \
    clienteMenu, detalleCliente, pagoCliente, \
    reservaCliente, \
    principal
    
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

    path('administracion/menus/index-producto/<id>/', indexMenusProductos, name="indexMenusProductos"),
    path('administracion/menus/registro-producto/<id>/', registroMenusProductos, name="registroMenusProductos"),
    path('administracion/menus/modificar-producto/<id>/', modificarMenusProductos, name="modificarMenusProductos"),
    path('crear-menus-productos/', crearMenusProductos, name="crearMenusProductos"),
    path('editar-menus-productos/', editarMenusProductos, name="editarMenusProductos"),

    path('administracion/insumos/', indexInsumos, name="indexInsumos"),
    path('crear-insumo/', crearInsumo, name="crearInsumo"),
    path('actualizar-insumo/', actualizarInsumos, name="actualizarInsumos"),
    path('administracion/insumos/registro/', registroInsumos, name="registroInsumos"),
    path('administracion/insumos/modificar/<id>/', modificarInsumos, name="modificarInsumos"),
    path('administracion/insumos/eliminar/<id>/', eliminarInsumos, name="eliminarInsumos"),

    path('administracion/productos/', indexProductos, name="indexProductos"),
    path('crear-producto/', crearProductos, name="crearProductos"),
    path('editar-producto/', editarProductos, name="editarProductos"),
    path('administracion/productos/registro/', registroProductos, name="registroProductos"),
    path('administracion/productos/modificar/<id>/', modificarProductos, name="modificarProductos"),
    path('administracion/productos/eliminar/<id>/', eliminarProductos, name="eliminarProductos"),

    path('administracion/mesas/', indexMesas, name="indexMesas"),
    path('crear-mesas/', crearMesas, name="crearMesas"),
    path('editar-mesas/', editarMesas, name="editarMesas"),
    path('administracion/mesas/eliminar/<id>/', eliminarMesas, name="eliminarMesas"),
    path('administracion/mesas/registro/', registroMesas, name="registroMesas"),
    path('administracion/mesas/modificar/<id>/', modificarMesas, name="modificarMesas"),
    
    path('administracion/recetas/', indexRecetas, name="indexRecetas"),
    path('crear-recetas/', crearRecetas, name="crearRecetas"),
    path('editar-recetas/', editarRecetas, name="editarRecetas"),
    path('administracion/recetas/eliminar/<id>/', eliminarRecetas, name="eliminarRecetas"),
    path('administracion/recetas/registro/', registroRecetas, name="registroRecetas"),
    path('administracion/recetas/modificar/<id>/', modificarRecetas, name="modificarRecetas"),

    path('administracion/recetas/index-ingredientes-recetas/<id>/', indexIngredientesRecetas, name="indexIngredientesRecetas"),
    path('administracion/recetas/registro-ingredientes-recetas/<id>/', registroIngredientesRecetas, name="registroIngredientesRecetas"),
    path('crear-ingredientes-recetas/', crearIngredientesRecetas, name="crearIngredientesRecetas"),

    path('administracion/pedidos-proveedor/', indexPedidosProveedor, name="indexPedidosProveedor"),
    path('administracion/pedidos-proveedor/detalle/<id>/', detallePedidosProveedor, name="detallePedidosProveedor"),
    path('autorizar-pedido/', autorizarPedidosProveedor, name="autorizarPedidosProveedor"),

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

    # TABLET CLIENTE
    path('cliente/clienteMenu/', clienteMenu, name="clienteMenu"),
    path('cliente/detalleCliente/', detalleCliente, name="detalleCliente"),
    path('cliente/pagoCliente/', pagoCliente, name="pagoCliente"),

    #RESERVA CLIENTE
    path('cliente/reservaCliente', reservaCliente, name="reservaCliente"),

    # PRINCIPAL
    path('cliente/principal', principal, name="principal"),

    # APIS URL MESAS
    

    # APIS URL
    #path('api/listar-proveedores/', api_views.ListarProveedoresAPIView.as_view() , name="listarProveedores"),
    
    path('api/listar-todo-mesas/', api_views.ListarTodoMesasAPIView.as_view() , name="todoMesas"),
    
    path('api/listar-mesas-disponibles/', api_views.ListarMesasDisponiblesAPIView.as_view() , name="mesasDisponibles"),
    
    path('api/listar-mesas-reservadas/', api_views.ListarMesasReservadasAPIView.as_view() , name="mesasReservadas"),
    
    path('api/listar-mesas-ocupadas/', api_views.ListarMesasOcupadasAPIView.as_view() , name="mesasOcupadas"),
    
    path('api/listar-ubicaciones/', api_views.ListarUbicacionesAPIView.as_view() , name="listarUbicaciones"),
    
    path('api/buscar-mesa/', api_views.BuscarMesaAPIView.as_view() , name="buscarMesa"),

    path('api/buscar-mesa-reserva/', api_views.BuscarMesaReservaAPIView.as_view() , name="buscarMesaReserva"),
    
    path('api/modificar-mesa/', api_views.ModificarMesaAPIView.as_view() , name="modificarMesa"),
    
    path('api/eliminar-mesa/', api_views.EliminarMesaAPIView.as_view() , name="eliminarMesa"),
    
    path('api/asignar-mesa/', api_views.AsignarMesaAPIView.as_view() , name="asignarMesa"),
    
    path('api/eliminar-asignacion/', api_views.EliminarAsignacionMesaAPIView.as_view() , name="eliminarAsignacion"),

]
