from .models import Proveedor
from rest_framework import serializers
from django.shortcuts import render
from django.db import connection

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'
    
    def listado_proveedor():
        django_cursor = connection.cursor()
        cursor = django_cursor.connection.cursor()
        out_cur = django_cursor.connection.cursor()

        cursor.callproc("PKG_PROVEEDOR.listarProveedor", [out_cur])

        lista= []
        for fila in out_cur:
            lista.append(fila)

        return lista