--EJERCICIOS UNION 


--EJERCICIO #1
--mostrar el total de registros de la tabla pasajero y pais en una misma consulta 

select  'País' as [Tabla],count(idpais) as [Total Registros] from pais  
union 
select 'Pasajeros',count(idpasajero) from PASAJERO