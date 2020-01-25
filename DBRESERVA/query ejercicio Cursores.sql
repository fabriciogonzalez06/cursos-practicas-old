--EJERCICIO #1 
--Implementar un cursor básico donde se imprima el primer registro de la tabla pasajero 

--crear cursor 
declare MICURSORPAS cursor 
FOR select *from PASAJERO

--APERTURAR EL CURSOR
open micursorpas

--acceder a los registros que ya están almacenados en el cursor 
fetch next from micursorpas

--cerrar cursor 
close micursorpas

--liberar cursor
deallocate micursorpas


--EJERCICIO #2 
--Implementar un cursor en donde se imprima en forma de reporte
--Los registros de la tabla pasajero 

--variables para almacenar los valores de las columnas 
declare @idpasajero char(8),@pasajero char(20),
@pais char(10),@documento char(12)

--declarar el cursor 
declare micursor cursor 
	for select pas.idpasajero,(pas.nombre + ' ' + pas.apaterno) as Pasajero,
	pai.nombre as [País] , pas.num_documento
	from pasajero pas inner join pais pai 
	on pas.idpais=pai.idpais

--abrir cursor 
open micursor

--obtener el primer registro y los valores mandarlos a las variables
fetch micursor into @idpasajero,@pasajero,@pais,@documento

--IMPRIMIR LA CABECERA DEL REPORTE 
print 'CÓDIGO     PASAJERO          PAÍS      DOCUMENTO'
PRINT '-----------------------------------------------------------'
--agregar los detalles del reporte
while @@FETCH_STATUS=0
begin
 
	print @idpasajero+space(5)+@pasajero+space(5)+
	@pais+space(5)+@documento

	--obtener la siguiente fila del cursor
	fetch micursor into @idpasajero,@pasajero,@pais,@documento
end

print '------------------------------------------------------------'
--cerrar cursor 
close micursor

--liberar el cursor 
deallocate micursor