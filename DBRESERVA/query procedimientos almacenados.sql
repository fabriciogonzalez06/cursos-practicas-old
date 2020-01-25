--PROCEDIMIENTOS ALMACENADOS DEL SISTEMA 

sp_columns pago
sp_column_privileges pais

sp_databases
sp_server_info

sp_fkeys pasajero--muestra donde se hacen referencias a la tabla pasaajero con su llave primaria 

sp_pkeys pasajero --muestra las llaves primarias de una tabla

--PROCEDIMIENTOS ALMACENADOS CREADOS 

--EJERCICIO #1 
--Implementar un procedimiento almacenado que muestre el listado de los paises y su total de pasajeros 

create proc totalPasajeros 
as
select pai.nombre as [País], count(pas.idpasajero) as TotalPasajeros
from PAIS pai inner join PASAJERO pas 
on pai.idpais=pas.idpais
group by pai.nombre 
order by pai.nombre asc
go

exec totalPasajeros


--EJERCICIO #2 
--Implementar un procedimiento almacenado que permita mostrar los pagos de un determinado pasajero 
--considerar para este caso como parametro de busqueda el número de documento del pasajero 

if object_id('pagosxpasajero') is not null
begin 
	drop procedure pagosxpasjero 
end 
go
create proc pagosxpasajero 
@num_documento varchar(30)
as 
select fecha,monto,tipo_comprobante,num_comprobante from pago where 
idpasajero=(select idpasajero from PASAJERO where num_documento=@num_documento)
go

select *from PASAJERO
exec  pagosxpasajero '47715777'


--EJERCICIO #3 
--Implementar un procedimiento almacenado que permita registrar un nuevo país 
--para este caso definir como parametros de entrada todos los campos referentes a la tabla pais 

if object_id('nuevopais') is not null
begin
	drop procedure nuevopais 
end
go

create procedure nuevopais 
@idpais char(4),
@nombre varchar(30)
as 
insert into PAIS(idpais,nombre)
values(@idpais,@nombre)
go

exec nuevopais'0014','Argelia'



--EJERCICIO #4 
--Implementar un procedimiento almacenado que retorne el total de pagos recibidos
--en una fecha determinada 

if OBJECT_ID('pagosxfecha') is not null
begin
drop procedure pagosxfecha
end 
go


create procedure pagosxfecha
@fecha date,
@total money output
as
	select @total=sum(monto) from pago 
	where fecha=@fecha
go

select *from pago
declare @t money 

exec pagosxfecha '20130505', @total=@t output
print 'Total '+space(4)+cast(@t as char(10))







