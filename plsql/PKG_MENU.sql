CREATE OR REPLACE 
PACKAGE PKG_MENU AS 

PROCEDURE crearMenu (p_nro_menu number, p_nom_menu varchar2, v_salida out number);
PROCEDURE crearDetalleMenu (p_id_menu number, p_id_producto number, p_descripcion varchar2, v_salida out number);
PROCEDURE modificarMenu (p_id_menu number, p_nro_menu number, p_nom_menu varchar2, v_salida out number);
PROCEDURE modificarDetalleMenu (p_id_det_menu number, p_id_producto number, p_descripcion varchar2, v_salida out number);
PROCEDURE listarMenu (p_cursor out sys_refcursor);
PROCEDURE listarDetalleMenu (p_id_menu number ,p_cursor out sys_refcursor);
PROCEDURE buscarMenu (p_id_menu number,p_nro_menu number, p_nom_menu varchar2, p_cursor out sys_refcursor);
PROCEDURE eliminarMenu (p_id_menu number, v_salida out number);
END PKG_MENU;

CREATE OR REPLACE
PACKAGE BODY PKG_MENU AS

  PROCEDURE crearMenu (p_nro_menu number, p_nom_menu varchar2, v_salida out number) AS
  BEGIN
    INSERT INTO MENU VALUES(SQ_MENU.NEXTVAL, p_nro_menu, p_nom_menu, 0);
    v_salida:=1;
    
    EXCEPTION
        WHEN OTHERS THEN
            v_salida:=0;
  END crearMenu;

  PROCEDURE crearDetalleMenu (p_id_menu number, p_id_producto number, p_descripcion varchar2, v_salida out number) AS
  BEGIN
    INSERT INTO DETALLE_MENU VALUES (SQ_DET_MENU.NEXTVAL,p_id_menu, p_id_producto,p_descripcion);
    v_salida:=1;
    
    EXCEPTION
        WHEN OTHERS THEN
            v_salida:=0;
  END crearDetalleMenu;

  PROCEDURE modificarMenu (p_id_menu number, p_nro_menu number, p_nom_menu varchar2, v_salida out number) AS
  BEGIN
    UPDATE MENU SET NRO_MENU = p_nro_menu, NOMBRE_MENU = p_nom_menu WHERE ID_MENU = p_id_menu;
    v_salida:=1;
    
    EXCEPTION
        WHEN OTHERS THEN
            v_salida:=0;
  END modificarMenu;

  PROCEDURE modificarDetalleMenu (p_id_det_menu number, p_id_producto number, p_descripcion varchar2, v_salida out number) AS
  BEGIN
    UPDATE DETALLE_MENU SET ID_PRODUCTO = p_id_producto, DESCRIPCION = p_descripcion;
    v_salida:=1;
    
    EXCEPTION 
        WHEN OTHERS THEN
            v_salida:=0;
  END modificarDetalleMenu;

  PROCEDURE listarMenu (p_cursor out sys_refcursor) AS
  BEGIN
    OPEN p_cursor FOR
        SELECT * FROM MENU;
  END listarMenu;

  PROCEDURE listarDetalleMenu (p_id_menu number ,p_cursor out sys_refcursor) AS
  BEGIN
    OPEN p_cursor FOR
        SELECT * FROM DETALLE_MENU WHERE ID_MENU = p_id_menu;
  END listarDetalleMenu;

  PROCEDURE buscarMenu (p_id_menu number,p_nro_menu number, p_nom_menu varchar2, p_cursor out sys_refcursor) AS
  v_menu number;
  v_nro_menu number;
  v_nombre varchar2(50);
  BEGIN
  IF v_menu > 0 and v_nro_menu = 0 and v_nombre = '' THEN
    OPEN p_cursor FOR
        SELECT * FROM MENU WHERE ID_MENU = p_id_menu;
  ELSIF v_menu = 0 and v_nro_menu > 0 and v_nombre = '' THEN
    OPEN p_cursor FOR
        SELECT * FROM MENU WHERE NRO_MENU = p_nro_menu;
  ELSIF v_menu = 0 and v_nro_menu = 0 and v_nombre != '' THEN
    OPEN p_cursor FOR
        SELECT * FROM MENU WHERE NOMBRE_MENU = p_nom_menu;
  END IF;
  END buscarMenu;
  

  PROCEDURE eliminarMenu (p_id_menu number, v_salida out number) AS
  BEGIN
    UPDATE MENU SET ID_EST_MENU = 2 WHERE ID_MENU = p_id_menu;
    v_salida:=1;
    
    EXCEPTION
        WHEN OTHERS THEN
            v_salida:=0;
  END eliminarMenu;

END PKG_MENU;