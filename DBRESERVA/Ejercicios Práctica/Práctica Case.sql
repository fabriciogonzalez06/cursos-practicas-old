--PRACTICA CASE 

--hacer un query donde muestre todos los pasajeros, donde solo muestre el nombre y el pais 
--y un mensaje si el mes de nacimiento es marzo mostrar un mensaje de ganador, en caso contrario normal 
select pas.nombre as [Nombre pasajero],pai.nombre as [País], 
case month(pas.fecha_nacimiento)
	when 3 then 
	'Ganador'
	else 
	'Normal' 
	end as [Estado] 
from PASAJERO pas inner join pais pai 
on pas.idpais=pai.idpais 


--EJERCICIO #2 
--mostrar todos los registros de la tabla montos junto con um mensaje que diga bienvenido siempre y cuando 
--la fecha de pago sea del año 2013

select *,case datepart(yy,fecha)
	when 2013 then 
	'Bienvenido'
	else 
	'*************'
	end as 'Mensaje'
  from pago 

select *from pago