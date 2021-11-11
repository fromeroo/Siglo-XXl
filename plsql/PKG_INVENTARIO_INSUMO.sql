create or replace NONEDITIONABLE PACKAGE PKG_INVENTARIO AS 
PROCEDURE crearInventario (p_id_ins number,p_stock number,p_fec_ven date,p_id_medida number,v_salida out number);
PROCEDURE editarStock (p_id_inv number, p_addStock number,v_salida out number);
PROCEDURE cambiarFecVencimiento (p_id_inv number, p_nueva_fecha date, v_salida out number);
PROCEDURE quitarInventario (p_id_inv number, v_salida out number);
PROCEDURE listarInventario (p_cursor out sys_refcursor);
PROCEDURE buscarInvInsumo (p_id_inv_ins number, p_cursor out sys_refcursor);
PROCEDURE listarUnidadMedida (p_cursor out sys_refcursor);

END PKG_INVENTARIO;

create or replace NONEDITIONABLE PACKAGE BODY PKG_INVENTARIO AS

  PROCEDURE crearInventario (p_id_ins number,p_stock number,p_fec_ven date,p_id_medida number,v_salida out number) AS
  BEGIN
    INSERT INTO INVENTARIO_INSUMO VALUES (SQ_INVENTARIO_INSUMO.NEXTVAL,p_id_ins,p_stock,p_fec_ven,p_id_medida,1);
    v_salida:=1;
    
    EXCEPTION
        WHEN OTHERS THEN
            v_salida:=0;
  END crearInventario;

  PROCEDURE editarStock (p_id_inv number, p_addStock number,v_salida out number) AS
  v_stockInicial number;
  v_nuevoStock number;
  BEGIN
    
    SELECT STOCK INTO v_stockInicial FROM INVENTARIO_INSUMO WHERE ID_INV_INS = p_id_inv;
    
    v_nuevoStock:= fn_aumentarstock(v_stockInicial,p_addStock);
    
    UPDATE INVENTARIO_INSUMO SET STOCK = v_nuevoStock WHERE ID_INV_INS = p_id_inv;
    v_salida:=1;
    
    EXCEPTION
        WHEN OTHERS THEN
            v_salida:=0;
  END editarStock;

  PROCEDURE cambiarFecVencimiento (p_id_inv number, p_nueva_fecha date, v_salida out number) AS
  BEGIN
    UPDATE INVENTARIO_INSUMO SET FEC_VENCIMIENTO = p_nueva_fecha WHERE ID_INV_INS = p_id_inv;
    v_salida:=1;
    
    EXCEPTION
        WHEN OTHERS THEN
            v_salida:=0;
  END cambiarFecVencimiento;

  PROCEDURE quitarInventario (p_id_inv number, v_salida out number) AS
  BEGIN
    UPDATE INVENTARIO_INSUMO SET ID_EST_INS = 2 WHERE ID_INV_INS = p_id_inv;
    v_salida:=1;
    
    EXCEPTION
        WHEN OTHERS THEN
            v_salida:=0;
  END quitarInventario;

  PROCEDURE listarInventario (p_cursor out sys_refcursor) AS
  BEGIN
  OPEN p_cursor FOR
    SELECT 
    A1.ID_INV_INS "ID INVENTARIO",
    A1.ID_INS "ID INSUMO",
    A2.NOM_INSUMO INSUMO,
    A1.STOCK STOCK,
    A1.FEC_VENCIMIENTO "FECHA DE VENCIMIENTO",
    A1.ID_UN_MED "ID MEDIDA",
    A3.DESC_UN_MED "UNIDAD DE MEDIDA",
    A1.ID_EST_INS "ID ESTADO",
    A4.DESC_EST_INS "ESTADO"    
    FROM INVENTARIO_INSUMO A1 JOIN INSUMO A2 ON A1.ID_INS=A2.ID_INS
    JOIN UNIDAD_MEDIDA A3 ON A1.ID_UN_MED=A3.ID_UN_MED
    JOIN EST_INVENTARIO_INSUMO A4 ON A1.ID_EST_INS=A4.ID_EST_INS
    WHERE A1.ID_EST_INS = 1;
  END listarInventario;

  PROCEDURE buscarInvInsumo (p_id_inv_ins number, p_cursor out sys_refcursor) AS
  BEGIN
    OPEN p_cursor FOR
    SELECT 
    A1.ID_INV_INS "ID INVENTARIO",
    A1.ID_INS "ID INSUMO",
    A2.NOM_INSUMO INSUMO,
    A1.STOCK STOCK,
    A1.FEC_VENCIMIENTO "FECHA DE VENCIMIENTO",
    A1.ID_UN_MED "ID MEDIDA",
    A3.DESC_UN_MED "UNIDAD DE MEDIDA",
    A1.ID_EST_INS "ID ESTADO",
    A4.DESC_EST_INS "ESTADO"    
    FROM INVENTARIO_INSUMO A1 JOIN INSUMO A2 ON A1.ID_INS=A2.ID_INS
    JOIN UNIDAD_MEDIDA A3 ON A1.ID_UN_MED=A3.ID_UN_MED
    JOIN EST_INVENTARIO_INSUMO A4 ON A1.ID_EST_INS=A4.ID_EST_INS
    WHERE A1.ID_INV_INS = p_id_inv_ins AND A1.ID_EST_INS = 1;
  
  END buscarInvInsumo;
  
  
  PROCEDURE listarUnidadMedida (p_cursor out sys_refcursor)
  AS
  BEGIN
    OPEN p_cursor FOR
        SELECT * FROM UNIDAD_MEDIDA;
  END;
  

END PKG_INVENTARIO;