create or replace NONEDITIONABLE PACKAGE PKG_INSUMO AS 

PROCEDURE crearInsumo (p_nom_insumo varchar2, p_id_tipo_insumo number, p_id_cat_insumo number, v_salida out number);
PROCEDURE listarInsumo (p_cursor out sys_refcursor);
PROCEDURE buscarInsumo (p_id_insumo number, p_nom_insumo varchar2, p_cursor out sys_refcursor);
PROCEDURE modificarInsumo (p_id_insumo number, p_nom_insumo varchar2, p_id_tipo_insumo number, p_id_cat_insumo number, v_salida out number);
PROCEDURE eliminarInsumo (p_id_insumo number, v_salida out number);
PROCEDURE listarTipoInsumo (p_cursor out sys_refcursor);
PROCEDURE listarCategoriaInsumo (p_cursor out sys_refcursor);


 
END PKG_INSUMO;

create or replace NONEDITIONABLE PACKAGE BODY PKG_INSUMO AS

  PROCEDURE crearInsumo (p_nom_insumo varchar2, p_id_tipo_insumo number, p_id_cat_insumo number, v_salida out number) AS
  BEGIN
    INSERT INTO INSUMO VALUES (SQ_INSUMO.NEXTVAL,p_nom_insumo,p_id_tipo_insumo,p_id_cat_insumo,1);
    v_salida:=1;
    
    EXCEPTION
        WHEN OTHERS THEN
            v_salida:=0;
  END crearInsumo;

  PROCEDURE listarInsumo (p_cursor out sys_refcursor) AS
  BEGIN
    OPEN p_cursor FOR
        SELECT 
        A1.ID_INS "ID INSUMO",
        A1.NOM_INSUMO "NOMBRE INSUMO",
        A1.ID_TIPO_INS "ID TIPO INSUMO",
        A4.DESC_TIPO_INS "DESCRIPCION TIPO INSUMO",
        A1.ID_CAT_INS "ID CATEGORIA",
        A3.NOM_CATEGORIA "NOMBRE CATEGORIA"
        FROM INSUMO A1 JOIN ESTADO_INSUMO A2 ON A1.ID_EST_INSUMO=A2.ID_EST_INSUMO
        JOIN CATEGORIA_INSUMO A3 ON A1.ID_CAT_INS=A3.ID_CAT_INS
        JOIN TIPO_INSUMO A4 ON A1.ID_TIPO_INS=A4.ID_TIPO_INS;
  END listarInsumo;

  PROCEDURE buscarInsumo (p_id_insumo number, p_nom_insumo varchar2, p_cursor out sys_refcursor) AS
  v_insumo number;
  v_nombre varchar2(50);
  BEGIN
   IF v_insumo > 0 and v_nombre ='' THEN
    OPEN p_cursor FOR
        SELECT 
        A1.ID_INS "ID INSUMO",
        A1.NOM_INSUMO "NOMBRE INSUMO",
        A1.ID_TIPO_INS "ID TIPO INSUMO",
        A4.DESC_TIPO_INS "DESCRIPCION TIPO INSUMO",
        A1.ID_CAT_INS "ID CATEGORIA",
        A3.NOM_CATEGORIA "NOMBRE CATEGORIA"
        FROM INSUMO A1 JOIN ESTADO_INSUMO A2 ON A1.ID_EST_INSUMO=A2.ID_EST_INSUMO
        JOIN CATEGORIA_INSUMO A3 ON A1.ID_CAT_INS=A3.ID_CAT_INS
        JOIN TIPO_INSUMO A4 ON A1.ID_TIPO_INS=A4.ID_TIPO_INS
        WHERE A1.ID_INS = v_insumo;
   ELSIF v_insumo = 0 and v_nombre != '' THEN
   OPEN p_cursor FOR
        SELECT 
        A1.ID_INS "ID INSUMO",
        A1.NOM_INSUMO "NOMBRE INSUMO",
        A1.ID_TIPO_INS "ID TIPO INSUMO",
        A4.DESC_TIPO_INS "DESCRIPCION TIPO INSUMO",
        A1.ID_CAT_INS "ID CATEGORIA",
        A3.NOM_CATEGORIA "NOMBRE CATEGORIA"
        FROM INSUMO A1 JOIN ESTADO_INSUMO A2 ON A1.ID_EST_INSUMO=A2.ID_EST_INSUMO
        JOIN CATEGORIA_INSUMO A3 ON A1.ID_CAT_INS=A3.ID_CAT_INS
        JOIN TIPO_INSUMO A4 ON A1.ID_TIPO_INS=A4.ID_TIPO_INS
        WHERE A1.NOM_INSUMO = v_nombre;
   END IF;
    
  END buscarInsumo;

  PROCEDURE modificarInsumo (p_id_insumo number, p_nom_insumo varchar2, p_id_tipo_insumo number, p_id_cat_insumo number, v_salida out number) AS
  BEGIN
    UPDATE INSUMO SET NOM_INSUMO = p_nom_insumo, ID_TIPO_INS = p_id_tipo_insumo, ID_CAT_INS = p_id_cat_insumo WHERE ID_INS = p_id_insumo;
    v_salida:=1;
    
    EXCEPTION
        WHEN OTHERS THEN
            v_salida:=0;
  END modificarInsumo;

  PROCEDURE eliminarInsumo (p_id_insumo number, v_salida out number) AS
  BEGIN
    UPDATE INSUMO SET ID_EST_INSUMO = 2 WHERE ID_INS = p_id_insumo;
    v_salida:=1;
    
    EXCEPTION
        WHEN OTHERS THEN
            v_salida:=0;
  END eliminarInsumo;
  
  PROCEDURE listarTipoInsumo (p_cursor out sys_refcursor)
  AS
  BEGIN
    OPEN p_cursor FOR
        SELECT * FROM TIPO_INSUMO;
  END;
  
  PROCEDURE listarCategoriaInsumo (p_cursor out sys_refcursor)
  AS
  BEGIN
    OPEN p_cursor FOR
        SELECT * FROM CATEGORIA_INSUMO;
  END;

END PKG_INSUMO;