--	EJERCICIO #1
--Implementar una función que devuelva el promedio de dos números ingresados por el usuario.


create function calcularpromedio 
(@valor1 as decimal(10,2),@valor2 as decimal(10,2))
returns decimal(10,2)
as
begin
	declare @promedio decimal(10,2)
	set @promedio=(@valor1+@valor2)/2 

	return @promedio
end
go

--probar funcion 
select dbo.calcularpromedio(4,5)

print 'Promedio ' + cast(dbo.calcularpromedio(12,13) as char(10))


--EJERCICIO #2 
--Implementar un función que devuelva una fecha ingresada en letras 
-- 05-05-2014 =  05 de mayo del 2014

if object_id('fechaletras') is not null
begin
 drop function fechaletras 
end
go

create function fechaletras
(@fecha as date)
returns varchar(40)
as 
begin

	declare @resultado varchar(40)

	set @resultado=CONCAT(DATENAME(dd,@fecha),' de ',datename(mm,@fecha),' del ',datename(yy,@fecha))
	return @resultado
end
go

--llamar funcion 
select dbo.fechaletras(GETDATE())

select nombre as [Nombre],amaterno as [Apellido Materno],apaterno as [Apellido Paterno],
dbo.fechaletras(fecha_nacimiento) as [Fecha Nacimiento] from PASAJERO
go
--EJERCICIO #3
--Implementar una función de tabla en línea que muestre los registros de la tabla pasajero 
--dependiendo del pais de providencia 

create function pasajerosxpais
(@pais as varchar(30))
returns table 
as 

		return  ( select pas.idpasajero ,(pas.nombre + ' ' + pas.apaterno) as 'Nombre',
		pai.nombre as [País] from 
		pasajero pas inner join pais pai on 
		pas.idpais=pai.idpais
		where pai.nombre=@pais)


select * from dbo.pasajerosxpais('Perú')


