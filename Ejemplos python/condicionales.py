print("Bienvenido a python")
numero1=20
numero2=30
numero3=40
#Esto es un comentario
#Calcular cual es el número mayor #Esto es el número mayor de tres números con if anidados 
if numero1>numero2 and numero1>numero3:
	print("El número mayor es ",numero1)
else:
	if numero2>numero1 and numero2>numero3:
		print("El número mayor es ",numero2)
	else:
	  if numero3>numero1 and numero3>numero2:
	  	print("El número mayor es ",numero3)
#Ahora con if independientes el numero menor de los tres 
if numero1<numero2 and numero1<numero3:
	print("El número menor es ",numero1)

if numero2<numero1 and numero2<numero3:
		print("El número menor es",numero2)

if numero3<numero1 and numero3<numero2:
			print("El número menor es ",numero3)	



		