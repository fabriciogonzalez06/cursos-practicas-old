--PRACTICA FUNCIONES 

--realizar una funcion que multiplique dos numeros 

create function multiplicar 
(@n1 as float,@n2 as float)
returns float 
as 
	begin
			declare @res float 
			
			set @res=@n1*@n2 

			return @res
	end 
go 

--utilizar función 
select dbo.multiplicar(3,3) as 'FuncionMultiplicar'


--EJERCICIO #3
--crear una funcion que reciba tres numeros y decida cual es el mayor 
create function num_mayor
(@n1 as float,@n2 as float,@n3 as float)
RETURNS float
as 
	begin	
		declare @mayor float
		
		if ((@n1>@n2) and (@n1>@n3))
		begin
			set @mayor=@n1 
		end  
		
		if ((@n2>@n1) and (@n2>@n3))
		begin
			set @mayor=@n2 
		end
		
		if ((@n3>@n1) and (@n3>@n2))
		begin
			set @mayor=@n3
		end
	
		return @mayor
	end 
go

--usar funcion 
declare  @n1 float=10,@n2 float =40.40,@n3 float =5

print 'El número mayor de ' + cast(@n1 as varchar(10))+space(5)+cast(@n2 as varchar(10))+
space(5)+cast(@n3 as varchar(10)) + ' es ' + cast(dbo.num_mayor(@n1,@n2,@n3) as char(15))
go



--EJERCICIO #3 
--Crear una funcion que reciba una fecha y que muestre el mes en palabras 
create function mes_a_palabras 
(@fecha as date)
returns varchar(50)
as 
begin
		--utilizar el case  
		return case datepart(MONTH,@fecha)
				when 1 then 'Enero'
				when 2 then 'Febrero'
				when 3 then 'Marzo'
				when 4 then 'Abril'
				when 5 then 'Mayo'
				when 6 then 'Junio'
				when 7 then 'Julio'
				when 8 then 'Agosto'
				when 9 then 'Septiembre'
				when 10 then 'Octubre'
				when 11 then 'Noviembre'
				when 12 then 'Diciembre'
				end
		 
end 
go

--implementar funcion mes_a_palabras 
select dbo.mes_a_palabras(SYSDATETIME()) as [Mes]


--EJERCICIO #4
--IMplementar un función que calcule el factorial de un número

create function factorial
(@num as numeric )
returns numeric
as 
begin
		
		declare @i int=1,@resultado numeric=1

		
		while @i<=@num
		begin
				 --operacion 
				 set @resultado=@resultado*@i

				 --incrementar i
				 set @i=@i+1
		end  

		--retornar el resultado 
		return @resultado
end 
go


--usar funcion 
select dbo.factorial(15) as [Factorial]


--hacer una funcion que retorne todos los pasajeros de un pais 
--se envia como parametro el pais

drop function pasajerosPais
create function PxP
(@pais as varchar(40))
returns table 
as 


	  return (select * from PASAJERO where 
				idpais=(select idpais from pais where nombre=@pais) )

go

--Implementar funcion 
declare @pais varchar(40)='Perú'

select * from dbo.PxP(@pais)
go



