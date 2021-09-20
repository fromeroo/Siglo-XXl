# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Banco(models.Model):
    id_bco = models.AutoField(primary_key=True)
    nom_bco = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'banco'


class Boleta(models.Model):
    id_bol = models.AutoField(primary_key=True)
    nro_boleta = models.IntegerField(unique=True)
    fec_emision = models.DateField()
    id_form_pago = models.ForeignKey('FormaPago', models.DO_NOTHING, db_column='id_form_pago')
    id_res_atencion = models.IntegerField()
    tiene_propina = models.CharField(max_length=1)
    id_porc_prop = models.ForeignKey('PorcPropina', models.DO_NOTHING, db_column='id_porc_prop')
    tiene_dcto = models.CharField(max_length=1)
    id_porc_dcto = models.ForeignKey('PorcDcto', models.DO_NOTHING, db_column='id_porc_dcto')
    valor_dcto = models.IntegerField()
    total = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'boleta'


class Caja(models.Model):
    id_caja = models.AutoField(primary_key=True)
    id_nro_caja = models.ForeignKey('NroCaja', models.DO_NOTHING, db_column='id_nro_caja')
    fec_hora_apertura = models.DateField()
    fec_hora_cierre = models.DateField()
    monto_apertura = models.IntegerField()
    id_est_caja = models.ForeignKey('EstCaja', models.DO_NOTHING, db_column='id_est_caja')
    id_usr = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usr')

    class Meta:
        managed = False
        db_table = 'caja'


class CategoriaInsumo(models.Model):
    id_cat_ins = models.AutoField(primary_key=True)
    nom_categoria = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'categoria_insumo'


class CategoriaProducto(models.Model):
    id_cat_prod = models.AutoField(primary_key=True)
    desc_cat_prod = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'categoria_producto'


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    rut_cli = models.IntegerField()
    dv = models.CharField(max_length=1)
    nom_cli = models.CharField(max_length=50)
    ap_pat_cli = models.CharField(max_length=100)
    ap_mat_cli = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=16)
    correo = models.CharField(max_length=100)
    fec_nac = models.DateField()

    class Meta:
        managed = False
        db_table = 'cliente'
        unique_together = (('rut_cli', 'correo'),)


class Comanda(models.Model):
    id_comanda = models.AutoField(primary_key=True)
    id_orden = models.ForeignKey('OrdenComida', models.DO_NOTHING, db_column='id_orden')
    id_est_comanda = models.ForeignKey('EstComanda', models.DO_NOTHING, db_column='id_est_comanda')
    fec_hora_ingreso = models.DateField()
    fec_hora_egreso = models.DateField()

    class Meta:
        managed = False
        db_table = 'comanda'


class Comuna(models.Model):
    id_com = models.AutoField(primary_key=True)
    nom_com = models.CharField(max_length=255)
    id_reg = models.ForeignKey('Region', models.DO_NOTHING, db_column='id_reg')

    class Meta:
        managed = False
        db_table = 'comuna'


class CuadraturaCaja(models.Model):
    id_cuadr = models.AutoField(primary_key=True)
    fec_cuadratura = models.DateField()
    monto_cuadrado = models.IntegerField()
    tuvo_descuadre = models.CharField(max_length=1)
    id_motivo_desc = models.ForeignKey('MotivoDescuadre', models.DO_NOTHING, db_column='id_motivo_desc', blank=True, null=True)
    monto_descuadre = models.IntegerField(blank=True, null=True)
    id_caja = models.ForeignKey(Caja, models.DO_NOTHING, db_column='id_caja')

    class Meta:
        managed = False
        db_table = 'cuadratura_caja'


class CuentaBancaria(models.Model):
    id_cuenta = models.AutoField(primary_key=True)
    nro_cta = models.BigIntegerField()
    nro_chip = models.BigIntegerField(blank=True, null=True)
    fec_expiracion = models.DateField()
    saldo_disp = models.IntegerField()
    sobregiro = models.IntegerField(blank=True, null=True)
    id_tipo_cuenta = models.ForeignKey('TipoCuenta', models.DO_NOTHING, db_column='id_tipo_cuenta')
    id_banco = models.ForeignKey(Banco, models.DO_NOTHING, db_column='id_banco')

    class Meta:
        managed = False
        db_table = 'cuenta_bancaria'
        unique_together = (('nro_cta', 'nro_chip'),)


class DetPed(models.Model):
    id_det_ped = models.AutoField(primary_key=True)
    id_ped = models.ForeignKey('Pedido', models.DO_NOTHING, db_column='id_ped')
    id_ins = models.ForeignKey('Insumo', models.DO_NOTHING, db_column='id_ins')
    cantidad = models.IntegerField()
    medida = models.CharField(max_length=255)
    id_marca = models.ForeignKey('MarcaInsumo', models.DO_NOTHING, db_column='id_marca')

    class Meta:
        managed = False
        db_table = 'det_ped'


class DetResAt(models.Model):
    id_det_res_at = models.AutoField(primary_key=True)
    id_res_at = models.ForeignKey('ResumenAtencion', models.DO_NOTHING, db_column='id_res_at')
    valor = models.IntegerField()
    cantidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'det_res_at'


class DetalleBoleta(models.Model):
    id_det_bol = models.AutoField(primary_key=True)
    id_bol = models.ForeignKey(Boleta, models.DO_NOTHING, db_column='id_bol')
    detalle = models.CharField(max_length=255)
    total = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'detalle_boleta'


class DetalleFactura(models.Model):
    id_det_fact = models.AutoField(primary_key=True)
    id_fact = models.ForeignKey('Factura', models.DO_NOTHING, db_column='id_fact')
    total_neto = models.IntegerField()
    iva = models.FloatField()
    total = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'detalle_factura'


class DetalleMenu(models.Model):
    id_det_menu = models.AutoField(primary_key=True)
    id_menu = models.ForeignKey('Menu', models.DO_NOTHING, db_column='id_menu')
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto')
    descripcion = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'detalle_menu'


class DetalleOc(models.Model):
    id_det_oc = models.AutoField(primary_key=True)
    id_oc = models.ForeignKey('OrdenCompra', models.DO_NOTHING, db_column='id_oc')
    neto_det = models.IntegerField()
    iva = models.FloatField()
    total_unit = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'detalle_oc'


class DetalleOrden(models.Model):
    id_det_orden = models.AutoField(primary_key=True)
    id_det_menu = models.ForeignKey(DetalleMenu, models.DO_NOTHING, db_column='id_det_menu')
    cantidad = models.IntegerField()
    id_orden_com = models.ForeignKey('OrdenComida', models.DO_NOTHING, db_column='id_orden_com')

    class Meta:
        managed = False
        db_table = 'detalle_orden'


class Direccion(models.Model):
    id_dir = models.AutoField(primary_key=True)
    calle = models.CharField(max_length=255)
    numeracion = models.IntegerField()
    nro_casa_depto = models.CharField(max_length=5, blank=True, null=True)
    tipo_dir = models.ForeignKey('TipoDireccion', models.DO_NOTHING, db_column='tipo_dir')
    id_com = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='id_com')

    class Meta:
        managed = False
        db_table = 'direccion'


class DireccionCliente(models.Model):
    id_dir = models.OneToOneField(Direccion, models.DO_NOTHING, db_column='id_dir', primary_key=True)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente')

    class Meta:
        managed = False
        db_table = 'direccion_cliente'
        unique_together = (('id_dir', 'id_cliente'),)


class DireccionProveedor(models.Model):
    id_proveedor = models.OneToOneField('Proveedor', models.DO_NOTHING, db_column='id_proveedor', primary_key=True)
    id_dir = models.ForeignKey(Direccion, models.DO_NOTHING, db_column='id_dir')

    class Meta:
        managed = False
        db_table = 'direccion_proveedor'
        unique_together = (('id_proveedor', 'id_dir'),)


class Disponibilidad(models.Model):
    id_disp = models.AutoField(primary_key=True)
    id_est_disp = models.ForeignKey('EstDisponibilidad', models.DO_NOTHING, db_column='id_est_disp')
    fec_disponible = models.DateField()
    hora_disponible = models.CharField(max_length=5)
    cant_persona = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'disponibilidad'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EstCaja(models.Model):
    id_est_caja = models.AutoField(primary_key=True)
    desc_est_caja = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'est_caja'


class EstComanda(models.Model):
    id_est_cmd = models.AutoField(primary_key=True)
    desc_est_cmd = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'est_comanda'


class EstDisponibilidad(models.Model):
    id_est_disp = models.AutoField(primary_key=True)
    desc_est_disp = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'est_disponibilidad'


class EstFormaPago(models.Model):
    id_est_forma_pago = models.AutoField(primary_key=True)
    desc_est_forma_pago = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'est_forma_pago'


class EstInsumo(models.Model):
    id_est_ins = models.AutoField(primary_key=True)
    desc_est_ins = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'est_insumo'


class EstOc(models.Model):
    id_est_oc = models.AutoField(primary_key=True)
    desc_est_oc = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'est_oc'


class EstOrden(models.Model):
    id_est_orden = models.AutoField(primary_key=True)
    desc_est_orden = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'est_orden'


class EstPedido(models.Model):
    id_est_ped = models.AutoField(primary_key=True)
    desc_est_ped = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'est_pedido'


class EstReceta(models.Model):
    id_est_rec = models.AutoField(primary_key=True)
    desc_est_rec = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'est_receta'


class EstadoFactura(models.Model):
    id_est_fact = models.AutoField(primary_key=True)
    desc_est_fact = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'estado_factura'


class EstadoMenu(models.Model):
    id_est_menu = models.AutoField(primary_key=True)
    desc_est_menu = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'estado_menu'


class EstadoMesa(models.Model):
    id_est_mesa = models.AutoField(primary_key=True)
    desc_est_mesa = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'estado_mesa'


class EstadoResAt(models.Model):
    id_est_res = models.AutoField(primary_key=True)
    desc_est_res_at = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'estado_res_at'


class EstadoReserva(models.Model):
    id_est_rsv = models.AutoField(primary_key=True)
    desc_est_rsv = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'estado_reserva'


class EstadoUsuario(models.Model):
    id_est_usr = models.AutoField(primary_key=True)
    desc_est_usr = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'estado_usuario'


class Factura(models.Model):
    id_factura = models.AutoField(primary_key=True)
    nro_factura = models.IntegerField(unique=True)
    fec_emision = models.DateField()
    fec_pago = models.DateField(blank=True, null=True)
    total_neto = models.IntegerField()
    iva = models.FloatField()
    total = models.IntegerField()
    id_oc = models.ForeignKey('OrdenCompra', models.DO_NOTHING, db_column='id_oc')
    id_forma_pago = models.ForeignKey('FormaPago', models.DO_NOTHING, db_column='id_forma_pago')
    id_est_factura = models.ForeignKey(EstadoFactura, models.DO_NOTHING, db_column='id_est_factura')

    class Meta:
        managed = False
        db_table = 'factura'


class FormaPago(models.Model):
    id_form_pago = models.AutoField(primary_key=True)
    desc_form_pago = models.CharField(max_length=100)
    id_est_form_pago = models.ForeignKey(EstFormaPago, models.DO_NOTHING, db_column='id_est_form_pago')

    class Meta:
        managed = False
        db_table = 'forma_pago'


class GiroProveedor(models.Model):
    id_giro_proveedor = models.AutoField(primary_key=True)
    desc_giro = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'giro_proveedor'


class Ingrediente(models.Model):
    id_ingrediente = models.AutoField(primary_key=True)
    id_insumo = models.ForeignKey('Insumo', models.DO_NOTHING, db_column='id_insumo')
    nom_ingrediente = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'ingrediente'


class Insumo(models.Model):
    id_ins = models.AutoField(primary_key=True)
    nom_insumo = models.CharField(max_length=100)
    id_tipo_ins = models.ForeignKey('TipoInsumo', models.DO_NOTHING, db_column='id_tipo_ins')
    id_cat_ins = models.ForeignKey(CategoriaInsumo, models.DO_NOTHING, db_column='id_cat_ins')

    class Meta:
        managed = False
        db_table = 'insumo'


class InventarioInsumo(models.Model):
    id_inv_ins = models.AutoField(primary_key=True)
    id_ins = models.ForeignKey(Insumo, models.DO_NOTHING, db_column='id_ins')
    stock = models.IntegerField()
    fec_vencimiento = models.DateField()
    id_un_med = models.ForeignKey('UnidadMedida', models.DO_NOTHING, db_column='id_un_med')
    id_est_ins = models.ForeignKey(EstInsumo, models.DO_NOTHING, db_column='id_est_ins')

    class Meta:
        managed = False
        db_table = 'inventario_insumo'


class LogError(models.Model):
    id_log = models.AutoField(primary_key=True)
    cod_error = models.CharField(max_length=255)
    desc_error = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'log_error'


class MarcaInsumo(models.Model):
    id_marca = models.AutoField(primary_key=True)
    nom_marca = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'marca_insumo'


class Menu(models.Model):
    id_menu = models.AutoField(primary_key=True)
    nro_menu = models.IntegerField()
    nombre_menu = models.CharField(max_length=50)
    id_est_menu = models.ForeignKey(EstadoMenu, models.DO_NOTHING, db_column='id_est_menu')

    class Meta:
        managed = False
        db_table = 'menu'


class Mesa(models.Model):
    id_mesa = models.AutoField(primary_key=True)
    nro_mesa = models.IntegerField()
    cant_sillas = models.IntegerField()
    id_ubicacion = models.ForeignKey('Ubicacion', models.DO_NOTHING, db_column='id_ubicacion')
    id_est_mesa = models.ForeignKey(EstadoMesa, models.DO_NOTHING, db_column='id_est_mesa')

    class Meta:
        managed = False
        db_table = 'mesa'


class MotivoDescuadre(models.Model):
    id_motivo = models.AutoField(primary_key=True)
    desc_mot = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'motivo_descuadre'


class MotivoRetiro(models.Model):
    id_motivo = models.AutoField(primary_key=True)
    desc_motivo = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'motivo_retiro'


class NroCaja(models.Model):
    id_no_caja = models.AutoField(primary_key=True)
    nro_caja = models.IntegerField()
    fec_creacion = models.DateField()

    class Meta:
        managed = False
        db_table = 'nro_caja'


class NvlAccPerfil(models.Model):
    id_nvl = models.AutoField(primary_key=True)
    desc_nvl = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'nvl_acc_perfil'


class OrdenComida(models.Model):
    id_ord_com = models.AutoField(primary_key=True)
    id_mesa = models.ForeignKey(Mesa, models.DO_NOTHING, db_column='id_mesa')
    fec_hora_inicio = models.DateField()
    fec_hora_termino = models.DateField()
    id_est_orden = models.ForeignKey(EstOrden, models.DO_NOTHING, db_column='id_est_orden')
    atendido_por = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='atendido_por')
    personas = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'orden_comida'


class OrdenCompra(models.Model):
    id_oc = models.AutoField(primary_key=True)
    nro_oc = models.CharField(max_length=100)
    total_neto_oc = models.IntegerField()
    iva = models.FloatField()
    total_oc = models.IntegerField()
    fec_oc = models.DateField()
    id_estado_oc = models.ForeignKey(EstOc, models.DO_NOTHING, db_column='id_estado_oc')
    id_pedido = models.ForeignKey('Pedido', models.DO_NOTHING, db_column='id_pedido', blank=True, null=True)
    dias_vigencia = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'orden_compra'


class Pedido(models.Model):
    id_ped = models.AutoField(primary_key=True)
    nro_pedido = models.IntegerField()
    fec_ped = models.DateField()
    id_est_ped = models.ForeignKey(EstPedido, models.DO_NOTHING, db_column='id_est_ped')
    id_proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='id_proveedor')
    id_usr = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usr')

    class Meta:
        managed = False
        db_table = 'pedido'


class Perfil(models.Model):
    id_perfil = models.AutoField(primary_key=True)
    desc_perfil = models.CharField(max_length=255)
    id_nvl = models.ForeignKey(NvlAccPerfil, models.DO_NOTHING, db_column='id_nvl')
    id_permiso = models.ForeignKey('Permiso', models.DO_NOTHING, db_column='id_permiso')

    class Meta:
        managed = False
        db_table = 'perfil'


class Permiso(models.Model):
    id_permiso = models.AutoField(primary_key=True)
    desc_permiso = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'permiso'


class PorcDcto(models.Model):
    id_porc_dcto = models.AutoField(primary_key=True)
    porc_dcto = models.FloatField()

    class Meta:
        managed = False
        db_table = 'porc_dcto'


class PorcPropina(models.Model):
    id_porc_prop = models.AutoField(primary_key=True)
    porc_prop = models.FloatField()

    class Meta:
        managed = False
        db_table = 'porc_propina'


class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    precio = models.IntegerField()
    id_cat_producto = models.ForeignKey(CategoriaProducto, models.DO_NOTHING, db_column='id_cat_producto')
    id_tipo_prod = models.ForeignKey('TipoProducto', models.DO_NOTHING, db_column='id_tipo_prod')
    id_receta = models.ForeignKey('Receta', models.DO_NOTHING, db_column='id_receta')

    class Meta:
        managed = False
        db_table = 'producto'


class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    rut_prv = models.IntegerField(unique=True)
    dv_prv = models.CharField(max_length=1)
    razon_social = models.CharField(max_length=255)
    nom_corto_prv = models.CharField(max_length=255)
    tlfn_prv = models.CharField(max_length=16)
    correo_prv = models.CharField(max_length=4000)
    id_giro = models.ForeignKey(GiroProveedor, models.DO_NOTHING, db_column='id_giro')

    class Meta:
        managed = False
        db_table = 'proveedor'


class Receta(models.Model):
    id_receta = models.AutoField(primary_key=True)
    nom_receta = models.CharField(max_length=100)
    id_est_receta = models.ForeignKey(EstReceta, models.DO_NOTHING, db_column='id_est_receta')
    tiempo_prep = models.IntegerField()
    temp_ideal = models.IntegerField()
    instrucciones = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'receta'


class RecetaIngrediente(models.Model):
    id_receta = models.OneToOneField(Receta, models.DO_NOTHING, db_column='id_receta', primary_key=True)
    id_ingrediente = models.ForeignKey(Ingrediente, models.DO_NOTHING, db_column='id_ingrediente')
    cant_ingrediente = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'receta_ingrediente'
        unique_together = (('id_receta', 'id_ingrediente'),)


class Region(models.Model):
    id_reg = models.AutoField(primary_key=True)
    nom_reg = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'region'


class Reserva(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    fec_reserva = models.DateField()
    fecha_hora_reserva = models.DateField()
    cant_asistentes = models.IntegerField()
    id_mesa = models.ForeignKey(Mesa, models.DO_NOTHING, db_column='id_mesa')
    id_est_reserva = models.ForeignKey(EstadoReserva, models.DO_NOTHING, db_column='id_est_reserva')
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente')
    id_disp = models.ForeignKey(Disponibilidad, models.DO_NOTHING, db_column='id_disp', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reserva'


class ResumenAtencion(models.Model):
    id_res_at = models.AutoField(primary_key=True)
    total_at = models.IntegerField()
    fec_hora_at = models.DateField()
    id_est_res_atencion = models.ForeignKey(EstadoResAt, models.DO_NOTHING, db_column='id_est_res_atencion')
    id_ord_com = models.ForeignKey(OrdenComida, models.DO_NOTHING, db_column='id_ord_com')

    class Meta:
        managed = False
        db_table = 'resumen_atencion'


class RetiroCaja(models.Model):
    id_retiro = models.AutoField(primary_key=True)
    fec_hora_retiro = models.DateField()
    id_motivo_ret = models.ForeignKey(MotivoRetiro, models.DO_NOTHING, db_column='id_motivo_ret')
    id_caja = models.ForeignKey(Caja, models.DO_NOTHING, db_column='id_caja')

    class Meta:
        managed = False
        db_table = 'retiro_caja'


class RevisionCaja(models.Model):
    id_caja = models.OneToOneField(Caja, models.DO_NOTHING, db_column='id_caja', primary_key=True)
    revisado_por = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='revisado_por')

    class Meta:
        managed = False
        db_table = 'revision_caja'
        unique_together = (('id_caja', 'revisado_por'),)


class TipoCuenta(models.Model):
    id_tipo_cta = models.AutoField(primary_key=True)
    desc_tipo_cta = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tipo_cuenta'


class TipoDireccion(models.Model):
    id_tipo_dir = models.AutoField(primary_key=True)
    desc_tipo_dir = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tipo_direccion'


class TipoInsumo(models.Model):
    id_tipo_ins = models.AutoField(primary_key=True)
    desc_tipo_ins = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tipo_insumo'


class TipoProducto(models.Model):
    id_tip_prod = models.AutoField(primary_key=True)
    desc_tipo_prod = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tipo_producto'


class TipoTransaccion(models.Model):
    id_tipo_trans = models.AutoField(primary_key=True)
    desc_trans = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tipo_transaccion'


class TransaccionBancaria(models.Model):
    id_transaccion = models.AutoField(primary_key=True)
    id_tipo_trans = models.ForeignKey(TipoTransaccion, models.DO_NOTHING, db_column='id_tipo_trans')
    id_cta_bco = models.ForeignKey(CuentaBancaria, models.DO_NOTHING, db_column='id_cta_bco')
    fec_transaccion = models.DateField()
    monto_transaccion = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'transaccion_bancaria'


class Ubicacion(models.Model):
    id_ubicacion = models.AutoField(primary_key=True)
    desc_ubicacion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'ubicacion'


class UnidadMedida(models.Model):
    id_un_med = models.AutoField(primary_key=True)
    desc_un_med = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'unidad_medida'


class Usuario(models.Model):
    id_usr = models.AutoField(primary_key=True)
    contrasenia = models.CharField(max_length=128)
    last_login = models.DateField()
    is_superuser = models.BooleanField()
    username = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateField()
    id_est_usr = models.ForeignKey(EstadoUsuario, models.DO_NOTHING, db_column='id_est_usr')
    id_perfil = models.ForeignKey(Perfil, models.DO_NOTHING, db_column='id_perfil')
    usuario_id_usr = models.ForeignKey('self', models.DO_NOTHING, db_column='usuario_id_usr', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'
        unique_together = (('username', 'email'),)


class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    fec_venta = models.DateField()
    id_bol = models.ForeignKey(Boleta, models.DO_NOTHING, db_column='id_bol')
    id_caja = models.ForeignKey(Caja, models.DO_NOTHING, db_column='id_caja')
    id_res_at = models.ForeignKey(ResumenAtencion, models.DO_NOTHING, db_column='id_res_at')

    class Meta:
        managed = False
        db_table = 'venta'
