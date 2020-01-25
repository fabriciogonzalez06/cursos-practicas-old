--#1 mostrar los registros de la tabla pasajero 
--ordenados de manera ascendente por su apellido parterno 

select all * from pasajero --todas la filas y todas las columnas 
order by apaterno asc

select idpasajero,nombre,apaterno,amaterno,num_documento from 
PASAJERO 

select idpasajero as Codigo,apaterno as ApellidoPaterno,amaterno as ApellidoMaterno
from PASAJERO

select idpasajero as [Código],nombre as Nombre, (apaterno + ' ' + amaterno) as Apellidos
from PASAJERO

--#2 Mostrar los 3 primeros registros de la tabal 
--PASAJERO ordenados por su apellido paternot 

select top 3 idpasajero as ID,nombre as Nombre,apaterno as ApellidoP,amaterno as ApellidoM
from PASAJERO
order by apaterno asc


--#3 Mostrar los 3 últimos registros de la tabla Pasajero
--ordenados ambos por apellidos 
select top 3 idpasajero as ID ,nombre as Nombre, apaterno as ApellidoP
,amaterno as ApellidoM from PASAJERO 
order by apaterno desc, amaterno desc--de manera desc son los ultimos

--Mostrar el 30% de los registros de la tabal Reserva
select top 30 percent * from RESERVA
go