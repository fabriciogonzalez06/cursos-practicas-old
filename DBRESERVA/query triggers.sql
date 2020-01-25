--EJERCICIO #1 
--Implementar un trigger que permita mostrar un mensaje cada vez que se inserte o actualice 
--un registro en la tabla pasajero.

create trigger trmensaje_pasajero
on pasajero 
for insert
as 
	print 'Pasajero registrado'
go
--
insert into pasajero 
values('P0000009','Luis','Arcilla','Diaz','DNI','8888888','19971206','0012','','luis@gmail.com','luis01')

--
alter trigger trmensaje_pasajero
on pasajero 
for insert,update
as 
	print 'Pasajero Actualizado'
go
--
update PASAJERO set nombre='Fabricio' 
where idpasajero='P0000009'

--EJERCICIO #2 
--Implementar un trigger que permita crear una replica de los registros insertados 
--en la tabla avion para dicho proceso implementar una nueva tabla llamada 
--avionBAK con las mismas columnas de la tabla avion 
create table avionBAK
(
idavion char(5) not null primary key,
idaeroline int not null,
fabricante varchar(40) null,
tipo varchar(30) not null,
capacidad int not null
)
go


if object_id('replicaavion') is not null
begin
	drop trigger replicaavion  
end 
go


create trigger tr_replicaavion
on avion 
after insert 
as 
begin
	insert avionBAK select * from inserted
end 

insert into AVION values('4','1','CHAirport','Comercial',250)
select *from avionbak

--EJERCICIO #3 
--Implementar un trigger que permita controlar el registro de un pago 
--se deberá evaluar que el monto a registrar sea mayor que cero en la columna monto de la tabla pago 

create trigger validapago 
on pago 
for insert 
as  
	if(select monto from inserted)<=0
	begin
		--negar la transcaccion 
		rollback transaction 
		print 'No se puede registrar monto 0' 
	end 
	else 
		print 'Pago registrado correctamente'

go 

--PROBAR TRIGGER 
insert into pago(idreserva,fecha,idpasajero,monto,tipo_comprobante,num_comprobante,impuesto)
values(1,getdate(),'P0000007',0,'Factura','0001-0004',0.18)

