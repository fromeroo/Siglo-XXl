from django.urls import path
from .views import indexUser, index, administrador, \
    registro

urlpatterns = [
    path('indexUser/', indexUser, name="indexUser"),
    path('', index, name="index"),
    path('administrador/', administrador, name="administrador"),
    path('registro/', registro, name="registro"),
]
