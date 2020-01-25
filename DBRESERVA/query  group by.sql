--EJERCICIO #1 
--Implementar un script que permita mostrar las claves primarias de la tabla pais 
--agrupadas desde la tabla pasajero group by 

select idpais as [País],count(idpais) as Cantidad from PASAJERO 
group by idpais 
go 

--EJERCICIO #2 
--Implementar un script que permita deternimar el total de aviones que tiene cada aerolinea y filtrar
--solo las aerolineas que tienen mas de un avion usar la clausula group by y having
select *from AEROLINEA
select *from AVION

select aer.nombre,count(avi.idavion) as Total_Aviones
from AEROLINEA aer inner join AVION avi on 
aer.idaerolinea=avi.idaerolinea 
group by aer.nombre
having count(avi.idavion)>1
go

select *from avion
insert into avion values('0001',1,'Taca','Comercial',200),
						('0002',2,'AirSport','Jet Privado',15),
						('0003',2,'AirSport','Comercial',100),
						('0004',5,'Taca','Comercial Jumbo',400),
						('0005',4,'VicaAvion','Comercial',250)



