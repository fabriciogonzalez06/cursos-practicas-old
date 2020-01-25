--EJERCICIO #1
--Hacer un procedimiento almacenado que busque todos ls pasajeros que empiecen con ciertos parametros 

create procedure spbuscar_pasajeros
@textobuscar varchar(40)
as 
select *from pasajero where 
nombre like @textobuscar + '%'
go
--Probar procedimiento almacenado 
execute spbuscar_pasajeros 'Jo'

--Ejercicio #2
--crear un procedimiento almacenado que devuleva cuantos aviones tiene una determinada aerolinea 

create proc spavionesXaerolinea
@aerolinea varchar(40),
@aviones int output
as
select @aviones=count(*) from AVION avi inner join 
	AEROLINEA aero on aero.idaerolinea=avi.idaerolinea
	group by aero.nombre 
	having aero.nombre=@aerolinea
go

declare @cant int 

exec spavionesXaerolinea 'LAN PERU',@aviones=@cant output 
print cast(@cant as varchar(10))

select *from aerolinea


