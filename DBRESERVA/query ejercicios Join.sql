--EJERCICIO #1	
--Implementar un script que permita mostrar los pasajeros con su correspondiente pais 
--de recidencia(inner join )

select pa.nombre As Nombre, (pa.apaterno + ' ' + pa.amaterno) as Apellidos, pai.nombre as [País]
from PASAJERO pa inner join PAIS pai on pa.idpais= pai.idpais


--EJERCICIO #2 
--Implementar un script que permita mostrar los pasajeros con las siguientes columnas 
--idpasajero,nombre, apaterno, amaterno, pís, fecha pago, monto de pago 

--tablas involucradas 
select *from pasajero 
select * from pais 
select * from pago

select pas.idpasajero,pas.nombre,pas.apaterno,pas.amaterno
,pai.nombre as [País],pag.fecha, pag.monto 
from pasajero pas inner join pais pai 
on pas.idpais=pai.idpais 
inner join pago pag on 
pas.idpasajero=pag.idpasajero
go

--EJERCICIO #3 
--Implementar un script que permita mostrar las reservas de un determinado pasajero 
-- especificado por su numero de documento. Finalmente debe ordenar la fecha de reserva de forma descendente

select *from PASAJERO

declare @num_documento varchar(12)='47715777'

select res.* 
from  pago pag inner join PASAJERO pas 
on pag.idpasajero=pas.idpasajero inner join 
RESERVA res on res.idreserva=pag.idreserva 
where pas.num_documento=@num_documento
order by res.fecha desc
go
