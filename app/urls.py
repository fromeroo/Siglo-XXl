from django.urls import path
from .views import indexUser, index, modificar_usuario, administrador, \
    registro, eliminar_usuario

urlpatterns = [
    path('indexUser/', indexUser, name="indexUser"),
    path('', index, name="index"),
    path('administrador/', administrador, name="administrador"),
    path('registro/', registro, name="registro"),
    path('modificar-usuario/<id>/', modificar_usuario, name='modificar_usuario'),
    path('indexUser/eliminar-usuario/<id>/', eliminar_usuario, name='eliminar_usuario'),
]
