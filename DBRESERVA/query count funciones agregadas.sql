--EJERCICIO #1 
--Implementar un script que permita determinar el total de pasajeros registrados 

select count(idpasajero) as [Total Pasajeros]from PASAJERO

--EJERCICIO #2 
--Implementar un script que permita determinar el total de pasajeros registrados agrupados por su pais 
--tener en cuenta las columnas a mostrar nombre del pais y total de pasajeros. Use la función agregada 
--count y la clausaula GROUP BY e INNER JOIN 

select pai.nombre as [País],count(pa.idpasajero) as [Total Pasajeros]
from pais pai inner join PASAJERO pa 
on pai.idpais=pa.idpais
group by pai.nombre


--EJERCICIO #3 
--Implementar un script que permita mostrar el total de pasajeros y el monto aculumalado
--de pagos de sus viajes realizados por un determinado país 

select pai.nombre as [País],count(pas.num_documento) as Total,sum(pag.monto) as [Total Acumulado]
from pais pai inner join PASAJERO pas on 
pai.idpais=pas.idpais inner join pago pag 
on pag.idpasajero=pas.idpasajero
group by pai.nombre
go
