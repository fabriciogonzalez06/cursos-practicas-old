--EJERCICIO #1 
--Implementar el Script que permita mostrar el precio promedio de las tarifas asignadas 
--a los siguientes vuelos 

select *from TARIFA

select avg(precio) as Promedio from TARIFA 

--EJERCICIO #2 
--implementar un Script que permita mostrar el monto promedio de pagos, agrupado por paises 
select *from pago

select *from PASAJERO 

select *from pais 

select pai.nombre as Pais,avg(pag.monto) as PromedioPais
from PAIS pai inner join PASAJERO pas on pai.idpais=pas.idpais
inner join pago pag on pas.idpasajero=pag.idpasajero
group by pai.nombre 
go


--EJERCICIO #2
--Implementar un script que permita mostrar los apellidos paternos de los pasajeros 
--y los nombres de los paises en una misma consulta  usari UNION

select pas.idpasajero as [Código],pas.apaterno as [Nombre] from pasajero pas 
union 
select pai.idpais , pai.nombre from pais pai
go

--EJERCICIO #3 
--Implementar un script que permita mostrar el total de registros de la tabla pasajeros,
--pais,pago desde una misma consulta 
select 'Pasajero' as [Tabla], count(idpasajero) as [Total Registros]
from PASAJERO 
union 
select 'País' as [Tabla],count(idpais) as [Total Registros]
from pais 
union 
select 'Pago' as [Tabla],count(idpago) as [Total Registros]
from pago
go
/*solo el primer alias el que cuenta al momento de buscar */
