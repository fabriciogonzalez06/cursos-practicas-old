--eliminar todos los registros de la tabla aerolinea

select *from AEROLINEA

begin tran 
delete from AEROLINEA
rollback tran

--eliminar el registro de la tabla pasajero cuyo idpasajero se P0000004
begin tran

delete from pasajero where
idpasajero='P0000004'

rollback tran

select *from PASAJERO


--eliminar los registros de la tabla pasajero cuyo país sea México,
--utilizar subconsultas 
select *from pasajero

begin tran

delete from pasajero 
where idpais=(select idpais from pais where nombre='México')

rollback tran

--Eliminar los registros de la tabla reserva que sean del año 2013
--y que no superen los 70 $
select *from RESERVA

begin tran
 
delete from reserva where 
datename(yy,fecha)='2013' and  costo<70

rollback tran

--eliminar los registros de la tabla PAGO que ser han efectuado
-- en el año 2012 ó 2013
select *from pago 

begin tran 

delete from pago where 
datepart(yy,fecha)=2012 or datepart(yy,fecha)=2013

rollback tran 

