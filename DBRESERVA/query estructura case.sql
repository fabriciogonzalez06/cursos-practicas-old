--EJERCICIO #1'
--Implementar un script que permita mostrar la fecha en texto 
--de la tabla reserva 
--2014-10-01  2014-octubre-01

select *,
cast(day(fecha) as char(2)) + 
case month(fecha)
	when 1 then ' Enero '
	when 2 then ' Febrero '
	when 3 then ' Marzo '
	when 4 then ' Abril '
	when 5 then ' Mayo '
	when 6 then ' Junio '
	when 7 then ' Julio '
	when 8 then ' Agosto '
	when 9 then ' Septiembre '
	when 10 then ' Octubre '
	when 11 then ' Noviembre '
	when 12 then ' Diciembre '
end 
+ cast(year(fecha) as char(4)) as [Fecha en Letras] 
from reserva
go

---EJERCICIO #2 
--Implementar un script que permita mostrar el número total de pasajeros por país 
--y el mensaje NO CUENTA solo a los paises cuyo número de pasajeros sea cero

select pai.nombre as [País],count(pas.idpasajero) as [Total Pasajeros],
case 
	when count(pas.idpasajero)=0 then ' NO CUENTA '
	else ' '
end  as [Mensaje]
from  pais pai left join 
pasajero pas on 
pas.idpais=pai.idpais
group by pai.nombre 
go  