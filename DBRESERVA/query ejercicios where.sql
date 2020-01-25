--#1 Script que permita mostrar los pasajeros cuyo tipo de 
--documento sea DNI

select *from pasajero 
where tip_documento='DNI'


--#2 mostrar los pagos que se han realizado 
--la fecha 27-01-2013

select all * from pago where 
fecha='20130127'

--#3 mostrar los pagos realizados en el mes de mayo del año 2014
select all * from pago 
where year(fecha)=2013 and month(fecha)=5

--#4 Mostrar los pasajeros que no tienen asignado un teléfono
select *from PASAJERO where 
telefono is  null

--#5 implementar un Script que permita mostrar 
--los pasajeros con su correspondiente país de residencia

select *from pais 
select *from pasajero 

select pas.*,pai.* from 
pasajero pas,pais pai
where pas.idpais=pai.idpais

select pas.nombre as Nombre,pas.apaterno as ApellidoP,pas.amaterno as ApellidoM,
pai.nombre as Pais 
from PASAJERO pas,PAIS pai
where pas.idpais=pai.idpais
