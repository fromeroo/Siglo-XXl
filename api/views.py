from django.db import connection
from rest_framework import generics
from rest_framework.response import Response
import cx_Oracle
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

class ListarGirosAPIView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        django_cursor = connection.cursor()
        cursor = django_cursor.connection.cursor()
        out_cur = django_cursor.connection.cursor()

        cursor.callproc("PKG_PROVEEDOR.listarGiros", [out_cur])

        lista= []
        for fila in out_cur:
            lista.append(fila)

        data = {
            'Giros': lista
        }
        
        return Response({
            'status': 200,
            'message': 'Dato recuperado exitosamente',
            'data': data
        })

class CrearPoveedorAPIView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        django_cursor = connection.cursor()
        cursor = django_cursor.connection.cursor()
        # out_cur = django_cursor.connection.cursor()
        
        rut = int(request.data["p_rut"])
        dv = request.data["p_dv"]
        razon_social = request.data["p_razon_social"]
        nombre_corto = request.data["p_nom_corto"]
        telefono = request.data["p_telefono"]
        correo = request.data["p_correo"]
        id_giro = int(request.data["p_id_giro"])
        direccion = request.data["p_direccion"]
        numero_dirrecion = int(request.data["p_num_dir"])
        numero_casa = int(request.data["p_nro_casa"])
        tipo_direccion = int(request.data["p_tipo_dir"])
        id_comuna= int(request.data["p_id_com"])
        

        cursor.callproc("PKG_PROVEEDOR.crearProveedores", [rut, dv, razon_social, nombre_corto, telefono, correo, id_giro, direccion, numero_dirrecion, numero_casa, tipo_direccion, id_comuna])

        # lista= []
        # for fila in out_cur:
        #     lista.append(fila)

        
        return Response({
            'status': 200,
            'message': 'Proveedor Creado'
        })