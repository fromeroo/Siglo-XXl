create or replace NONEDITIONABLE PACKAGE PKG_PROVEEDOR AS 

  /* TODO enter package declarations (types, exceptions, methods etc) here */ 
PROCEDURE crearProveedores (p_rut number, p_dv varchar2, p_razon_social varchar2, p_nom_corto varchar2,
                            p_telefono varchar2, p_correo varchar2, p_id_giro number, p_direccion varchar2,p_num_dir number,
                            p_nro_casa number, p_tipo_dir number, p_id_com number, v_salida out number);
PROCEDURE modificarProveedor (p_id_proveedor number, p_razon_social varchar2, p_nom_corto varchar2,
                            p_telefono varchar2, p_correo varchar2, p_id_giro number, v_salida out number);
PROCEDURE listarProveedor (p_cursor out SYS_REFCURSOR);
PROCEDURE buscarProveedor (p_id_proveedor number, p_cursor out sys_refcursor);
PROCEDURE eliminarProveedor (p_id_proveedor number,v_salida out number);
PROCEDURE listarGiros (p_cursor out sys_refcursor);


END PKG_PROVEEDOR;

create or replace NONEDITIONABLE PACKAGE BODY PKG_PROVEEDOR AS

  PROCEDURE crearProveedores (p_rut number, p_dv varchar2, p_razon_social varchar2, p_nom_corto varchar2,
                            p_telefono varchar2, p_correo varchar2, p_id_giro number, p_direccion varchar2,p_num_dir number,
                            p_nro_casa number, p_tipo_dir number, p_id_com number, v_salida out number) AS
  BEGIN
    -- TAREA: Se necesita implantación para PROCEDURE PKG_PROVEEDOR.crearProveedores
    INSERT INTO DIRECCION VALUES (SQ_DIRECCION.NEXTVAL, p_direccion, p_num_dir, p_nro_casa, p_tipo_dir, p_id_com);
    INSERT INTO PROVEEDOR VALUES (SQ_PROVEEDOR.NEXTVAL, p_rut, p_dv, p_razon_social, p_nom_corto, p_telefono, p_correo, p_id_giro,1);
    INSERT INTO DIRECCION_PROVEEDOR VALUES (SQ_PROVEEDOR.CURRVAL, SQ_DIRECCION.CURRVAL);
    v_salida:=1;
    
    EXCEPTION
        WHEN OTHERS THEN
        v_salida:=0;
    
  END crearProveedores;

  PROCEDURE modificarProveedor (p_id_proveedor number, p_razon_social varchar2, p_nom_corto varchar2,
                            p_telefono varchar2, p_correo varchar2, p_id_giro number, v_salida out number) AS
  
  BEGIN
  
    -- TAREA: Se necesita implantación para PROCEDURE PKG_PROVEEDOR.modificarProveedor
    UPDATE PROVEEDOR SET RAZON_SOCIAL = p_razon_social, NOM_CORTO_PRV = p_nom_corto, TLFN_PRV = p_telefono,
                         CORREO_PRV = p_correo, ID_GIRO = p_id_giro WHERE ID_PROVEEDOR = p_id_proveedor;
            v_salida:=1;
    EXCEPTION
        WHEN OTHERS THEN
            v_salida:=0;
    
  END modificarProveedor;

  PROCEDURE listarProveedor (p_cursor out SYS_REFCURSOR) AS
  BEGIN
    -- TAREA: Se necesita implantación para PROCEDURE PKG_PROVEEDOR.listarProveedor
   OPEN p_cursor FOR
    SELECT 
        A1.ID_PROVEEDOR "ID PROVEEDOR",
        A1.NOM_CORTO_PRV NOMBRE,
        A1.RUT_PRV || '-' || A1.DV_PRV RUT,
        A1.RAZON_SOCIAL "RAZÓN SOCIAL",
        A1.TLFN_PRV TELEFONO,
        A1.CORREO_PRV CORREO,
        A1.ID_GIRO "ID GIRO",
        A2.DESC_GIRO GIRO,
        A1.ID_EST_PROVEEDOR "ID ESTADO PROVEEDOR",
        A3.DESC_EST_PROVEEDOR "ESTADO PROVEEDOR"
    FROM PROVEEDOR A1 JOIN GIRO_PROVEEDOR A2 ON A1.ID_GIRO=A2.ID_GIRO_PROVEEDOR
    JOIN ESTADO_PROVEEDOR A3 ON A1.ID_EST_PROVEEDOR=A3.ID_EST_PROVEEDOR
    WHERE A1.ID_EST_PROVEEDOR = 1;
        
  END listarProveedor;

  PROCEDURE buscarProveedor (p_id_proveedor number, p_cursor out sys_refcursor) AS
  
  BEGIN
   
    -- TAREA: Se necesita implantación para PROCEDURE PKG_PROVEEDOR.buscarProveedor
    OPEN p_cursor FOR
    SELECT 
        A1.NOM_CORTO_PRV NOMBRE,
        A1.RUT_PRV || '-' || A1.DV_PRV RUT,
        A1.RAZON_SOCIAL "RAZÓN SOCIAL",
        A1.TLFN_PRV TELEFONO,
        A1.CORREO_PRV CORREO,
        A2.DESC_GIRO GIRO,
        A1.ID_EST_PROVEEDOR "ID ESTADO PROVEEDOR",
        A3.DESC_EST_PROVEEDOR "ESTADO PROVEEDOR"
    FROM PROVEEDOR A1 JOIN GIRO_PROVEEDOR A2 ON A1.ID_GIRO=A2.ID_GIRO_PROVEEDOR
    JOIN ESTADO_PROVEEDOR A3 ON A1.ID_EST_PROVEEDOR=A3.ID_EST_PROVEEDOR
    WHERE A1.ID_PROVEEDOR = p_id_proveedor and A1.ID_EST_PROVEEDOR = 1;
    
    
  END buscarProveedor;

  PROCEDURE eliminarProveedor (p_id_proveedor number,v_salida out number) AS
  BEGIN
    UPDATE PROVEEDOR SET ID_EST_PROVEEDOR = 2 WHERE ID_PROVEEDOR = p_id_proveedor;
    v_salida:=1;
    
    EXCEPTION
        WHEN OTHERS THEN
            v_salida:=0;
  END eliminarProveedor;
  
  PROCEDURE listarGiros (p_cursor out sys_refcursor)
  AS
  BEGIN
    OPEN p_cursor FOR
        SELECT * FROM GIRO_PROVEEDOR;
  END listarGiros;

END PKG_PROVEEDOR;