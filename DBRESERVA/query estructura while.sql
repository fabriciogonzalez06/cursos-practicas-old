--EJERCICIO #1 
--Implementar un script que permita mostrar los números pares consecutivos del 1 al 100 

--declarar variable 
declare @n int=0

while (@n<100)
begin 
	--incrementar n
	set @n=@n+1

	--preguntar si es par y mostrarlo 
	if (@n % 2=0)
		begin
			print 'El valor ' + cast(@n as char(2))
		end

	
end 
go

--EJERCICIO #2
--Implementar un escript que permita aumentar en un 10% el costo de las tarifas solo si el promedio 
--de estas no supera los 2000 cuando se termine de actualizar los valores mostrar un mensaje 
--YA NO HAY MAS QUE ACTUALIZAR 


select *from TARIFA 

while (select avg(precio) from tarifa )<2000
begin
		update tarifa set precio=precio + (precio*0.10)
		
		if(select max(precio) from TARIFA)>2000
		
			begin
			
			break 
			
			end 
		else
		 
		begin

		continue
		 
		end
		 
end

print 'Ya no hay más que actualizar'
go





