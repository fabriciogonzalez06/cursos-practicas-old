--PRÁCTICA WHILE 

--EJERCICIO #1 
--hacer un programa que muestre los numeros pares hasta un determinado número 

declare @numero int =500, @i int =0

while @i<@numero
begin

	if (@i % 2=0)
	begin
		print cast(@i as char(5)) 
	end	 
	--Incrementar contador 
	set @i=@i+1
end 
go


--EJERCICIO #2 
--de la tabla tarifa disminuir el 10% en el campo precio para todos los registros mientras no se baje de 500

while (select min(precio) from tarifa)>500
begin
   
   --disminuir el 10% 
   update tarifa set precio=precio -(precio*0.10)
end 
print 'Todo actualizado'
go

select *from tarifa

