
--EJERCICIO #1
--Script que permita verificar si un determinado país 
--fue registrado o no en su tabla de origen

select *from pais 

declare @pais varchar(40)
set @pais='Perú'
--ver si existe 
if exists(select idpais from pais where nombre=@pais)
	print 'País ya se encuentra registrado '
else
	print 'El país no se encuentra registrado'

--EJERCICIO #2
--Script que permite mostrar los pasajeros cuyo nombre inicie con la letra A
select *from pasajero where nombre like 'A%'

--EJERCICIO #3 
--Mostrar los pasajeros que tienen una cuenta de correo GMAIL
select *from pasajero where email like '%gmail%'

--EJERCICIO #4 
--Mostrar los pasajeros cuyo segundo carácter de su nombre sea la letra A,O ó U
select *from pasajero where nombre like '_[AOU]%'
go

--EJERCICIO #5 
--Mostrar los pasajeros cuyo segundo carácter de su nombre NO sea la letra A,O ó U
select *from pasajero where nombre  like '_[^AOU]%'--exponente significa no pueden estar las siguientes letras
go


--EJERCICIO #6 
--Mostrar los pagos realizados por un determinado pasajero,filtrar a dicho pasajero 
--por su número de documento usar subconsultas operadores T-SQL

select * from pasajero

declare @documento varchar(40)
set @documento='47715777'

select *from pago where 
idpasajero=(select idpasajero from PASAJERO where num_documento=@documento)