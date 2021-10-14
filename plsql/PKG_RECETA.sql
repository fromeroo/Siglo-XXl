CREATE OR REPLACE 
PACKAGE PKG_RECETA AS 

PROCEDURE crearReceta (p_nom_receta varchar2,p_tiempo_prep varchar2,p_temp_ideal varchar2,p_instrucciones varchar2,
                       p_id_ingrediente number,p_cant_ingrediente number,v_salida out number);
PROCEDURE listarReceta (p_cursor out sys_refcursor);
PROCEDURE buscarReceta (p_id_receta number,p_nom_receta varchar2, p_cursor out sys_refcursor);
PROCEDURE modificarReceta (p_id_receta number, p_nom_receta varchar2,p_tiempo_prep varchar2,p_temp_ideal varchar2,p_instrucciones varchar2,v_salida out number);
PROCEDURE eliminarReceta (p_id_receta number, v_salida out number);
PROCEDURE listarIngredientes (p_cursor out sys_refcursor);
PROCEDURE listarIngredientesReceta (p_id_receta number, p_cursor out sys_refcursor);

END PKG_RECETA;

CREATE OR REPLACE
PACKAGE BODY PKG_RECETA AS

  PROCEDURE crearReceta (p_nom_receta varchar2,p_tiempo_prep varchar2,p_temp_ideal varchar2,p_instrucciones varchar2,
                         p_id_ingrediente number,p_cant_ingrediente number,v_salida out number) AS
  BEGIN
    INSERT INTO RECETA VALUES (SQ_RECETA.NEXTVAL,p_nom_receta,1,p_tiempo_prep,p_temp_ideal,p_instrucciones);
    INSERT INTO RECETA_INGREDIENTE VALUES (SQ_RECETA.CURRVAL,p_id_ingrediente,p_cant_ingrediente);
    v_salida:=1;
    
    EXCEPTION 
        WHEN OTHERS THEN
            v_salida:=0;
  END crearReceta;

  PROCEDURE listarReceta (p_cursor out sys_refcursor) AS
  BEGIN
    OPEN p_cursor FOR
        SELECT 
        A1.ID_RECETA "ID RECETA",
        A1.NOM_RECETA "NOMBRE RECETA",
        A1.ID_EST_RECETA "ID ESTADO RECETA",
        A2.DESC_EST_REC "ESTADO RECETA",
        A1.TIEMPO_PREP "TIEMPO DE PREPARACIÓN",
        A1.TEMP_IDEAL "TEMPERATURA IDEAL (°C)",
        A1.INSTRUCCIONES INSTRUCCIONES
        FROM RECETA A1 JOIN EST_RECETA A2 ON A1.ID_EST_RECETA=A2.ID_EST_REC;
  END listarReceta;

  PROCEDURE buscarReceta (p_id_receta number,p_nom_receta varchar2, p_cursor out sys_refcursor) AS
  BEGIN
    IF p_id_receta > 0 and p_nom_receta = '' THEN
        OPEN p_cursor FOR
        SELECT 
        A1.ID_RECETA "ID RECETA",
        A1.NOM_RECETA "NOMBRE RECETA",
        A1.ID_EST_RECETA "ID ESTADO RECETA",
        A2.DESC_EST_REC "ESTADO RECETA",
        A1.TIEMPO_PREP "TIEMPO DE PREPARACIÓN",
        A1.TEMP_IDEAL "TEMPERATURA IDEAL (°C)",
        A1.INSTRUCCIONES INSTRUCCIONES
        FROM RECETA A1 JOIN EST_RECETA A2 ON A1.ID_EST_RECETA=A2.ID_EST_REC
        WHERE A1.ID_RECETA = p_id_receta;
    ELSIF p_id_receta = 0 and p_nom_receta != '' THEN
        OPEN p_cursor FOR
        SELECT 
        A1.ID_RECETA "ID RECETA",
        A1.NOM_RECETA "NOMBRE RECETA",
        A1.ID_EST_RECETA "ID ESTADO RECETA",
        A2.DESC_EST_REC "ESTADO RECETA",
        A1.TIEMPO_PREP "TIEMPO DE PREPARACIÓN",
        A1.TEMP_IDEAL "TEMPERATURA IDEAL (°C)",
        A1.INSTRUCCIONES INSTRUCCIONES
        FROM RECETA A1 JOIN EST_RECETA A2 ON A1.ID_EST_RECETA=A2.ID_EST_REC
        WHERE A1.NOM_RECETA = p_nom_receta;
    END IF;
        
  END buscarReceta;

  PROCEDURE modificarReceta (p_id_receta number, p_nom_receta varchar2,p_tiempo_prep varchar2,p_temp_ideal varchar2,p_instrucciones varchar2,v_salida out number) AS
  BEGIN
    UPDATE RECETA SET NOM_RECETA = p_nom_receta, TIEMPO_PREP = p_tiempo_prep, TEMP_IDEAL = p_temp_ideal, INSTRUCCIONES = p_instrucciones
                      WHERE ID_RECETA = p_id_receta;
    v_salida:=1;
    EXCEPTION
        WHEN OTHERS THEN
            v_salida:=0;
  END modificarReceta;

  PROCEDURE eliminarReceta (p_id_receta number, v_salida out number) AS
  BEGIN
    UPDATE RECETA SET ID_EST_RECETA = 2 WHERE ID_RECETA = p_id_receta;
    v_salida:=1;
    
    EXCEPTION
        WHEN OTHERS THEN
            v_salida:=0;
  END eliminarReceta;
  
  PROCEDURE listarIngredientes (p_cursor out sys_refcursor)
  AS
  BEGIN
    OPEN p_cursor FOR
        SELECT * FROM INGREDIENTE;
  END;
  
  PROCEDURE listarIngredientesReceta (p_id_receta number, p_cursor out sys_refcursor)
  AS
  BEGIN
    OPEN p_cursor FOR
        SELECT 
        A2.NOM_INGREDIENTE "INGREDIENTE",
        A3.NOM_INSUMO "INSUMO",
        A1.CANT_INGREDIENTE "CANTIDAD"
        FROM RECETA_INGREDIENTE A1 
        JOIN INGREDIENTE A2 ON A1.ID_INGREDIENTE=A2.ID_INGREDIENTE
        JOIN INSUMO A3 ON A2.ID_INSUMO=A3.ID_INS
        WHERE A1.ID_RECETA = p_id_receta;
  END;

END PKG_RECETA;