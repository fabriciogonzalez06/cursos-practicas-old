--EJERCICIO #1
--Implementar un script que permita mostrar un acumulado de los montos registrados en la tabla pago(SUM)
select *from pago

select sum(monto) from pago 

--EJERCICIO #2 
--Implementar un script que permita mostrar el acumulado de los montos 
--registrados en la tabla pago por cada año, considere el año de la columna fecha,
--use sum y group bay
select year(fecha) AS "Año",sum(monto) as "Total Año" from pago 
group by year(fecha)
go

--EJERCICIO #3 
--Implementar un script que permita mostrar el acumulado de los montos registrados en la tabla pagos
--por cada año y mes, considere el año de la columna fecha use la función SUM y la Cláusula Group by

select year(fecha) as [Año],month(fecha) as Mes,sum(monto) as Total
from PAGO 
group by year(fecha),month(fecha)
order by year(fecha) desc, month(fecha) desc
go

select *from PAGO