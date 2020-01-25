--EJERCICIO #1	
--Implementar un script que permita mostrar los pasajeros que no han realizado ningun 
--pago (left join)

select pas.* from 
PASAJERO pas left join pago pag 
on pas.idpasajero=pag.idpasajero 
where pag.idpasajero is null
go 

select *from pago

--EJERCICIO #2 
--Implementar un Script que permita mostrar todos los registros de la tabla pasajero  y pais right join
select pai.nombre as [País], pas.* 
from PASAJERO pas right join pais pai 
on pas.idpais=pai.idpais
go


--EJERCICIO #3 
--Implementar un script que permita mostrar los registros de la tabla pasajero y pago de tal forma que se aplique 
--un producto cartesiano entre sus filas(cross join)
select pas.*,pag.* from PASAJERO pas cross join pago pag 
go