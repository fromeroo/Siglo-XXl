from django.urls import path
from .views import indexUser, index, indexProveedores, registroProveedores, modificarProveedores, indexMenus, \
    indexProductos, indexRecetas, indexPedidosProveedor, indexStockProductos, indexGestionCajaFinanzas, indexGestionCajas, \
    indexGestionFacturas,indexDetalleUtilidades, indexPagoEfectivo ,indexMesas, indexTablero, modificar_usuario, \
    administrador, dashboard, registro, eliminar_usuario, registroProductos, modificarProductos, registroRecetas, \
    modificarRecetas, registroMenus, modificarMenus, registroGestionCajas, modificarGestionCajas, registroMesas, modificarMesas, \
    registroStockProductos, modificarStockProductos, registroGestionFacturas, modificarGestionFacturas

urlpatterns = [
    path('', index, name="index"),
    path('administrador/', administrador, name="administrador"),

    path('administracion/usuario/registro/', registro, name="registro"),
    path('administracion/usuario/', indexUser, name="indexUser"),
    path('administracion/usuario/eliminar/<id>/', eliminar_usuario, name='eliminar_usuario'),
    path('administracion/usuario/modificar/<id>/', modificar_usuario, name='modificar_usuario'),

    path('administracion/proveedores/', indexProveedores, name="indexProveedores"),
    path('administracion/proveedores/registro/', registroProveedores, name="registroProveedores"),
    path('administracion/proveedores/modificar/<id>/', modificarProveedores, name="modificarProveedores"),

    path('administracion/menus/', indexMenus, name="indexMenus"),
    
    path('administracion/menus/registro/', registroMenus, name="registroMenus"),

    path('administracion/menus/modificar/<id>/', modificarMenus, name="modificarMenus"),

    path('administracion/productos/', indexProductos, name="indexProductos"),
    path('administracion/productos/registro/', registroProductos, name="registroProductos"),
    path('administracion/productos/modificar/<id>/', modificarProductos, name="modificarProductos"),

    path('administracion/recetas/', indexRecetas, name="indexRecetas"),

    path('administracion/mesas/', indexMesas, name="indexMesas"),
    
    path('administracion/mesas/registro/', registroMesas, name="registroMesas"),
    
    path('administracion/mesas/modificar/<id>/', modificarMesas, name="modificarMesas"),
    path('administracion/recetas/registro/', registroRecetas, name="registroRecetas"),
    path('administracion/recetas/modificar/<id>/', modificarRecetas, name="modificarRecetas"),

    path('administracion/pedidos-proveedor/', indexPedidosProveedor, name="indexPedidosProveedor"),

    path('administracion/menus/', indexMenus, name="indexMenus"),

    path('administracion/mesas/', indexMesas, name="indexMesas"),

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

    path('finanzas/detalle-utilidades/', indexDetalleUtilidades, name="indexDetalleUtilidades"),

    path('caja/pago-efectivo/', indexPagoEfectivo, name="indexPagoEfectivo"),

    path('cocina/tablero/', indexTablero, name="indexTablero"),

    path('dashboard/', dashboard, name="dashboard"),
]
