

declare @pi float
declare @radio float
declare @area float
--valores iniciales 
set @pi=3.1415
set @radio=7

--encontrar el area del cierculo 
--set @area=@pi*@radio*@radio;--manera 1

set @area=@pi * power(@radio,2)--manera 2

select @area as [Área] 
go

--Script que permita capturar en una variable
--el correo electronico del pasajero con codigo
--P0000005, usar variables transct-SQL y sentencia select para mostrar email
declare @correo varchar(70)

select @correo=email from pasajero 
where idpasajero='P0000005'

select 'P0000005' as [Código], @correo as Email
go


--Mi manera 
declare @correo varchar(70)

set @correo=(select email from PASAJERO where idpasajero='P0000005')

select @correo as Correo