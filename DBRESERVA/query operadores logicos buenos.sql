--Ejercicio 1 
--Script para mostrar las reservas que sean del año 2014 y no 
--superen los $ 500

select *from reserva 
where year(fecha)=2014 and 
costo<500

select *from reserva

--Ejercicio 2 
--Script que permita mostrar las reservas cuyo 
--costo se encuentre desde 400 hasta 700

select *from reserva where 
costo between 400 and 700


--Ejercicio #3 
--Script que permita mostrar los pasajeros cuya letra
--inicial de su apellido paterno se encuentre entre a y c 
select *from PASAJERO 
where LEFT(apaterno,1) between 'A' and 'C'--left extrae el primer caracter de derecha a izquierda 
order by apaterno desc,amaterno asc,nombre asc
go
--Ejercicio #4 
--Script que permita mostrar los pasajeros cuya letra inicial 
--de su apellido paterno no se encuentre entre a y c 
select *from PASAJERO 
where not LEFT(apaterno,1) between 'A' and 'C'--left extrae el primer caracter de derecha a izquierda 
order by apaterno desc,amaterno asc,nombre asc
go

--#5 Script que permita mostrar las reservas 
--cuya fecha se encuentra en el año 2013

