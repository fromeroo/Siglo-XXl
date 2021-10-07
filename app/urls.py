from django.urls import path
from .views import indexUser, index, indexProveedores, registroProveedores, modificarProveedores, indexMenus, registroMenus, modificarMenus, indexProductos, indexRecetas, indexPedidosProveedor, indexStockProductos, indexGestionCajaFinanzas, indexGestionCajas, registroGestionCajas, modificarGestionCajas , indexGestionFacturas,indexDetalleUtilidades, indexPagoEfectivo ,indexMesas, registroMesas, modificarMesas, indexTablero, modificar_usuario, administrador, dashboard, \
    registro, eliminar_usuario 

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

    path('administracion/recetas/', indexRecetas, name="indexRecetas"),

    path('administracion/mesas/', indexMesas, name="indexMesas"),
    
    path('administracion/mesas/registro/', registroMesas, name="registroMesas"),
    
    path('administracion/mesas/modificar/<id>/', modificarMesas, name="modificarMesas"),

    path('administracion/pedidos-proveedor/', indexPedidosProveedor, name="indexPedidosProveedor"),

    path('administracion/gestion-cajas/', indexGestionCajas, name="indexGestionCajas"),
    
    path('administracion/gestion-cajas/registro/', registroGestionCajas, name="registroGestionCajas"),
    
    path('administracion/gestion-cajas/modificar/<id>/', modificarGestionCajas, name="modificarGestionCajas"),

    path('bodega/stock-productos/', indexStockProductos, name="indexStockProductos"),

    path('finanzas/gestion-caja/', indexGestionCajaFinanzas, name="indexGestionCajaFinanzas"),

    path('finanzas/gestion-facturas/', indexGestionFacturas, name="indexGestionFacturas"),

    path('finanzas/detalle-utilidades/', indexDetalleUtilidades, name="indexDetalleUtilidades"),

    path('caja/pago-efectivo/', indexPagoEfectivo, name="indexPagoEfectivo"),

    path('cocina/tablero/', indexTablero, name="indexTablero"),

    path('dashboard/', dashboard, name="dashboard"),
]
