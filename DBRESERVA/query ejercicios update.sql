--Actualizar los valores de la columna impuesto
--por el valor 11 a todos los registros de la tabla tarifa

select *from tarifa

update tarifa set 
impuesto=11
go

--aumentar en dos el impuesto de ta tabla tarifa
update tarifa set 
impuesto =impuesto +2 
go

--asignar el impuesto a cero solo a los registros cuya clase sea 
--Econ�mici de la tabla tarifa
update tarifa set 
impuesto=0 
where clase='Econ�mica'
go

--actualizar los costos de la tabla reserva 
--disminuyendo en 50 a los registros cuyo ingreso se realizo 
--en el a�o 2013, utilizar variables
select *from reserva

declare @monto money=50
update RESERVA set costo=costo-@monto
where year(fecha)=2013
go

--asignar el texto 'SIN FONO' en el campo tel�fono de los pasajeros
--que sean de Per� todo esto deber� ser realizado en la tabla pasajero.

select *from pasajero

update PASAJERO set telefono='SIN FONO'
where idpais=(select idpais from pais where nombre='Per�')
go
