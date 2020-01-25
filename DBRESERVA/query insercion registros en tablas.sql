--insertar registros en la tabla reserva
insert into RESERVA(idreserva,costo,fecha,observacion)
values('1','140','2013-01-27','')
go

insert into RESERVA(idreserva,costo,fecha,observacion)
values('2','100','2013-01-01','')
go

insert into RESERVA(idreserva,costo,fecha,observacion)
values('3','300','2014-04-03','')
go

insert into RESERVA(idreserva,costo,fecha,observacion)
values('4','800','2014-05-04','')
go

insert into RESERVA(idreserva,costo,fecha,observacion)
values('5','250',getdate(),'')
go


insert into RESERVA(idreserva,costo,fecha,observacion)
values('6','150',getdate(),'')
go

insert into RESERVA(idreserva,costo,fecha,observacion)
values('7','700',getdate(),'')
go

--TABLA PAGO 
insert into pago(idreserva,fecha,idpasajero,monto,tipo_comprobante,num_comprobante,impuesto)
values('1','2013-01-27','P0000001',100,'Factura','0001-0001',0.18)
go

insert into pago(idreserva,fecha,idpasajero,monto,tipo_comprobante,num_comprobante,impuesto)
values('1','20130127','P0000001',40,'Ticket','0001-0007',0.18),
('5','20130505','P0000002',250,'Factura','0001-0002',0.18),
('7',getdate(),'P0000007',700,'Factura','0001-0003',0.18)
go

select *from pago


--INSERTAR TABLA TARIFA
insert into TARIFA
values ('1','Supervip',12,1200),
('2','Vip',12,1000),
('3','Nacional',12,800),
('4','Económica',0,500)
go

--INSERTAR REGISTROS EN LA TABLA AEROPUERTO
insert into AEROPUERTO(idaeropuerto,idpais,nombre)
values('AE01','0003','Bariloche'),
('AE02','0003','Mar del Plata'),
('AE03','0001','Jorge Chávez')
go

select *from aeropuerto



