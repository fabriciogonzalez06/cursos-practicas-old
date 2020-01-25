--EJERCICIO #1 
--Implementar un script que permita mostrar el monto mas alto y mas bajo registrado en la tabla pago 

select max(monto) as [Monto mayor],min(monto) as [Monto menor ] from pago
go

--EJERCICIO #2
--Implementar un Script que permita mostrar los montos m�s altos y mas bajos por a�o de la tabla 
--pago ordenados de forma descentente
select year(fecha) as [A�o],max(monto) as [Monto mayor],min(monto) as [Monto menor]
from pago 
group by year(fecha)
order by year(fecha) desc
go 

--EJERCICIO #3 
--Implementar un script que permita mostrar los datos del pasajero que registra el mayor monto de la la tabla pago

declare @maxPago money
select @maxPago=max(monto) from pago 

select pas.* 
from PASAJERO pas 
where pas.idpasajero=(select idpasajero from pago where monto=@maxPago)
go
