#Un generador en python crea una instancia de un objeto y consume menos recursos que una función 

def generarPares(limite):
	i=1

	while i<=limite:
		#condición para saber si es par 
		if i%2==0:
			#Aquí si es par lo almacena y lo pausa con la instrucción yield
			yield i

		#Aumentar contador 
		i+=1



lim=int(input("\n Hasta donde desea saber los pares >"))
#Validar datos correctos 
while lim<=0:
	print("\n Error, valor no válido, Ingrese nuevamente ")
	lim=int(input("\n Hasta donde desea saber los pares >"))

#Crear objeto que obtendra los valores devueltos por el yield de una función este paso es muy importante
devuelvePares=generarPares(lim)		
#Imprimir tamaño del objeto devuelve pares 
#print(len(devuelvePares))  NO SE PUEDE APLICAR EN GENERADORES CONOCER EL TAMAÑO DE EL OBJETO 



#utilizar el next para devolver lo que tiene el objeto generador 
print(next(devuelvePares))



#Devuelve el siguiente elemento de el objeto devuelve pares con next 

print(next(devuelvePares))