from django.db import connection
from rest_framework import generics
from rest_framework.response import Response
import cx_Oracle


# APIS MESAS
class ListarTodoMesasAPIView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        django_cursor = connection.cursor()
        cursor = django_cursor.connection.cursor()
        out_cur = django_cursor.connection.cursor()

        cursor.callproc("PKG_MESA.listarTodoMesa", [out_cur])

        lista= []
        for fila in out_cur:
            lista.append(fila)

        data = {
            'MesasTodas': lista
        }
        
        return Response({
            'status': 200,
            'message': 'Dato recuperado exitosamente',
            'data': data
        })

class ListarMesasDisponiblesAPIView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        django_cursor = connection.cursor()
        cursor = django_cursor.connection.cursor()
        out_cur = django_cursor.connection.cursor()

        cursor.callproc("PKG_MESA.listarMesasDisponibles ", [out_cur])

        lista= []
        for fila in out_cur:
            lista.append(fila)

        data = {
            'MesasDisponibles': lista
        }
        
        return Response({
            'status': 200,
            'message': 'Dato recuperado exitosamente',
            'data': data
        })

class ListarMesasReservadasAPIView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        django_cursor = connection.cursor()
        cursor = django_cursor.connection.cursor()
        out_cur = django_cursor.connection.cursor()

        cursor.callproc("PKG_MESA.listarMesasReservadas", [out_cur])

        lista= []
        for fila in out_cur:
            lista.append(fila)

        data = {
            'MesasReservadas': lista
        }
        
        return Response({
            'status': 200,
            'message': 'Dato recuperado exitosamente',
            'data': data
        })
class ListarMesasOcupadasAPIView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        django_cursor = connection.cursor()
        cursor = django_cursor.connection.cursor()
        out_cur = django_cursor.connection.cursor()

        cursor.callproc("PKG_MESA.listarMesaOcupada", [out_cur])

        lista= []
        for fila in out_cur:
            lista.append(fila)

        data = {
            'MesasOcupadas': lista
        }
        
        return Response({
            'status': 200,
            'message': 'Datos recuperado exitosamente',
            'data': data
        })

class ListarUbicacionesAPIView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        django_cursor = connection.cursor()
        cursor = django_cursor.connection.cursor()
        out_cur = django_cursor.connection.cursor()

        cursor.callproc("PKG_MESA.listarUbicaciones", [out_cur])

        lista= []
        for fila in out_cur:
            lista.append(fila)

        data = {
            'Ubicaciones': lista
        }
        
        return Response({
            'status': 200,
            'message': 'Datos recuperado exitosamente',
            'data': data
        })

class BuscarMesaAPIView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        django_cursor = connection.cursor()
        cursor = django_cursor.connection.cursor()
        
        p_id_mesa= int(request.data["p_id_mesa"])
        out_cur = django_cursor.connection.cursor()
        
        cursor.callproc("PKG_MESA.buscarMesa", [p_id_mesa, out_cur])

        lista= []
        for fila in out_cur:
            lista.append(fila)
        
        if not lista:
            return Response({
                'status': 400,
                'message': 'Mesa No Encontrada'
            })

        return Response({
            'status': 200,
            'message': 'Mesa Encontrada',
            'data': lista
        })
class BuscarMesaReservaAPIView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        django_cursor = connection.cursor()
        cursor = django_cursor.connection.cursor()
        
        p_reserva= int(request.data["p_reserva"])
        out_cur = django_cursor.connection.cursor()
        
        cursor.callproc("PKG_MESA.buscarMesaReserva", [p_reserva, out_cur])

        lista= []
        for fila in out_cur:
            lista.append(fila)
        
        if not lista:
            return Response({
                'status': 400,
                'message': 'Mesa Reservada No Encontrada'
            })

        return Response({
            'status': 200,
            'message': 'Mesa Reservada Encontrada',
            'data': lista
        })

class ModificarMesaAPIView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        django_cursor = connection.cursor()
        cursor = django_cursor.connection.cursor()
        
        p_id_mesa = int(request.data["p_id_mesa"])
        p_nro_mesa = int(request.data["p_nro_mesa"])
        p_cant_sillas = int(request.data["p_cant_sillas"])
        p_id_ubi = int(request.data["p_id_ubi"])
        v_salida = cursor.var(cx_Oracle.NUMBER)
        
        cursor.callproc("PKG_MESA.modificarMesa", [p_id_mesa, p_nro_mesa, p_cant_sillas, p_id_ubi, v_salida])

        res = v_salida.getvalue()

        if res == 1:
            return Response({
                'status': 400,
                'message': 'Error al modificar Mesa'
            })
        else:
            return Response({
                'status': 200,
                'message': 'Mesa Modificada'
            })

class EliminarMesaAPIView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        django_cursor = connection.cursor()
        cursor = django_cursor.connection.cursor()
        
        p_id_mesa = int(request.data["p_id_mesa"])
        v_salida = cursor.var(cx_Oracle.NUMBER)
        
        cursor.callproc("PKG_MESA.eliminarMesa", [p_id_mesa, v_salida])

        res = v_salida.getvalue()

        if res == 1:
            return Response({
                'status': 400,
                'message': 'Error al modificar Mesa'
            })
        else:
            return Response({
                'status': 200,
                'message': 'Mesa Modificada'
            })


class AsignarMesaAPIView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        django_cursor = connection.cursor()
        cursor = django_cursor.connection.cursor()
    
        p_id_mesa = int(request.data["p_id_mesa"])
        v_salida = cursor.var(cx_Oracle.NUMBER)
        
        cursor.callproc("PKG_MESA.asignarMesa", [p_id_mesa, v_salida])

        res = v_salida.getvalue()

        if res == 1:
            return Response({
                'status': 200,
                'message': 'Mesa Asignada'
            })
        else:
            return Response({
                'status': 400,
                'message': 'Error al asignar Mesa'
            })

class EliminarAsignacionMesaAPIView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        django_cursor = connection.cursor()
        cursor = django_cursor.connection.cursor()
    
        p_id_mesa = int(request.data["p_id_mesa"])
        v_salida = cursor.var(cx_Oracle.NUMBER)
        
        cursor.callproc("PKG_MESA.eliminarAsignacionMesa", [p_id_mesa, v_salida])

        res = v_salida.getvalue()

        if res == 1:
            return Response({
                'status': 200,
                'message': 'Asignacion Eliminada'
            })
        else:
            return Response({
                'status': 400,
                'message': 'Error al eliminar Asignacion'
            })
            