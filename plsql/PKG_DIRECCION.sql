create or replace NONEDITIONABLE PACKAGE PKG_DIRECCION AS 

PROCEDURE listarComunas(p_cursor out sys_refcursor);
PROCEDURE listarRegiones (p_cursor out sys_refcursor);
PROCEDURE listarTipoDireccion (p_cursor out sys_refcursor);
  /* TODO enter package declarations (types, exceptions, methods etc) here */ 

END PKG_DIRECCION;

create or replace NONEDITIONABLE PACKAGE BODY PKG_DIRECCION AS

  PROCEDURE listarComunas(p_cursor out sys_refcursor) AS
  BEGIN
    OPEN p_cursor FOR
        SELECT ID_COM, NOM_COM FROM COMUNA; 
  END listarComunas;

  PROCEDURE listarRegiones (p_cursor out sys_refcursor) AS
  BEGIN
    OPEN p_cursor FOR
        SELECT ID_REG, NOM_REG FROM REGION; 
  END listarRegiones;

  PROCEDURE listarTipoDireccion (p_cursor out sys_refcursor)
  AS
  BEGIN
    OPEN p_cursor FOR
        SELECT * FROM TIPO_DIRECCION;
  END listarTipoDireccion;

END PKG_DIRECCION;