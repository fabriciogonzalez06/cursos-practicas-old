#Este programa crea una lista de números pares mediante una función 
def generarPares(limite):
	#Crear lista vacía 
	lista=[]
	i=1

	while i<=limite:

		#Agregar elementos a la lista con i 
		if i%2==0:
			lista.append(i)

		#Aumentar contador 
		i+=1
	return lista
	

#Programa principal 
limite=int(input("\n Ingrese hasta donde desea saber los números pares >"))
#Validar no ingresar números negativos 
while limite<=0:
	print("\n Error, valor no válido ingrese nuevamente por favor >")
	limite=int(input("\n Ingrese hasta donde desea saber los números pares >"))

#Llamar a la función y guardar eso en una variable 

listaGenerada=generarPares(limite)

#Imprimir lista 
print(listaGenerada)				