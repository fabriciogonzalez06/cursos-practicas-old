--EJERCICIO #1 
--crear un trigger que cada ves que se borre un registro de la tabla aerolinea cree una copia 
--en una tabla llamada aerolineBAK
if exists(select *from sysobjects where name='aerolineaBAK')
begin
 drop table aerolineaBAK
end 
go
create table aerolineaBAK
(
idaerolinea int ,
ruc char(11),
nombre varchar(40)
)

--crear trigger
create trigger tr_copia_aerolineaBAK
on aerolinea 
after delete 
as 
begin
	insert into aerolineaBAK select * from deleted 
end
go

insert into AEROLINEA(idaerolinea,ruc,nombre) 
select 6,'1010101010','PACA'

--borrar y probar triger 
delete from aerolinea where idaerolinea=6

select *from aerolineaBAK

select *from aerolinea

--Ejercicio #2 
--cree un trigger que despues de haber borrado un pais lo guarde en una tabla llamada 
--paisBAK y tambien guarde la fecha que fue borrado 

drop table paisBAK

create table paisBAK
(
idpais char(4),
nombre varchar(30),
fecha datetime default sysdatetime()
)

drop trigger tr_copia_paisBAK
--crear trigger 
create trigger tr_copia_paisBAK
on pais 
after delete 
as 
begin
	insert into paisBAK(idpais,nombre) select idpais,nombre from deleted 
end 
go

select *from pais 

--insertar un pais 
insert into pais(idpais,nombre) select '0013','Camerún'

delete from PAIS where idpais='0013'

--ver tabla recovery 
select *from paisBAK
order by idpais


