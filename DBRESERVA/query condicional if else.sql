--EJERCICIO #1
--Implementar un script que permita insertar un nuevo registro 
--en la tabla pa�s en caso se registre una duplicidad en el nombre de un pais mostrar un mensaje de 
--pais ya registrado en caso contrario insertar dicho registro y mostrar un mensaje de 
--pa�s registrado exitosamente 
select *from pais

--Declarar variables 
declare @idpais char(4)='0012',
@nombre varchar(30)='Jap�n'

if exists(select idpais from pais where nombre=@nombre)
	begin
	--no se puede manejar que la las cadenas no sean equals o iguales no distingue entre mayusculas o minusculas
		print 'Pa�s ya registrado' 
	end
else 
	begin 
		insert into pais(idpais,nombre)
		values(@idpais,@nombre)
		--mensaje de insertado correctamente
		print 'Insertado correctamente'
	end
end
go

--OTRA MANERA 
declare @idpais char(4)='0011',
@nombre varchar(30)='PER�'

if exists (select idpais from pais where idpais=@idpais) or exists(select idpais from pais where nombre=@nombre)
begin
	print 'Error, El Pa�s o la llave primaria ya existen' 
end 
else 
begin
	insert into pais(idpais,nombre)
	values(@idpais,@nombre)
	print 'Agregado Correctamente'
end
go

select *from pais 
order by  idpais asc


--EJERCICIO #2
--Implementar un script que permita mostrar el mensaje de no hay pasajeros en este pa�s, solo cuando el total de pasajeros
--asignados a un determinado pa�s no tenga registros en la tabla pasajero 
--caso contrario determinar cuantos pasajeros tiene dicho pais 

declare @pais char(40)='Bolivia'
if  (select count(*) from PASAJERO pas left join pais pai 
	on pai.idpais=pas.idpais 
	group by pai.nombre 
	having pai.nombre=@pais ) is null
begin
	print 'NO hay pasajeros en este pa�s'
end 
else
begin
	--declarar variable para almacenar pasajeros 
	declare @total int

	select @total=count(*) from PASAJERO pas 
	left join pais pai on pas.idpais=pai.idpais 
	group by pai.nombre 
	having pai.nombre=@pais

	--mostrar resultado
	print 'El pa�s ' + @pais + ' Tiene ' + 	cast(@total as char(2)) + ' Pasajeros'

end 
go

select datename(mm,fecha)from reserva


