--	PRACTICA IF 

select all * from pasajero
order by idpasajero

--EJERCICIO #1 
--hacer un query que no permita ingresar un idpasajero existente, de lo contrario si no existe permitir la insercion 
--tambien verificar si el pais existe o no 

--declarar variables 
declare @idpasajero char(8)='P0000012',@nombre varchar(20)='Jose',@apaterno varchar(20)='Martinez',
@amaterno varchar(20)='Díaz',@tipo_documento varchar(30)='DNI',@num_documento varchar(12)='199700065',
@fecha_nacimiento date=getdate(),@idpais char(4)='0005',@telefono varchar(15)='',@email varchar(50)='jose@gmail.com.hn',
@clave varchar(20)='Jose01'

if not exists(select idpais from pais where idpais=@idpais)
begin
	print 'El código del país no existe ' 
end 
else 
if exists(select idpasajero from PASAJERO where idpasajero=@idpasajero)
begin
	print 'Este pasajero ya existe 
	' 
end 
	else
begin
	insert into PASAJERO(idpasajero,nombre,apaterno,amaterno,tip_documento,num_documento
	,fecha_nacimiento,idpais,telefono,email,clave) 
	select @idpasajero,@nombre,@apaterno,@amaterno,@tipo_documento,@num_documento,
	@fecha_nacimiento,@idpais,@telefono,@email,@clave
	
	print 'Insertado correctamente' 
end 	 
go


--EJERCICIO #2
--Hacer un query que reciba el pais y muestre si hay pasajeros en ese pais o no 


declare @pais varchar(20)='Bolivia'

if (select count(*) from PASAJERO pas inner join 
	PAIS pai on pas.idpais=pai.idpais 
	group by pai.nombre
	having pai.nombre=@pais) is null
begin
	print 'Este país no tiene pasajeros' 
end
	else
begin
	declare @cant int 
	
	select @cant=count(*) from PASAJERO pas inner join 
	PAIS pai on pas.idpais=pai.idpais 
	group by pai.nombre
	having pai.nombre=@pais 

	print 'El país '+ @pais + ' tiene '  + cast(@cant as char(10) ) + 'Pasajeros'
end 
go





