from django.db import connection
from rest_framework import generics
from rest_framework.response import Response
# Create your views here.

class ListarProveedoresAPIView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
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
        
        return Response({
            'status': 200,
            'message': 'Dato recuperado exitosamente',
            'data': data
        })