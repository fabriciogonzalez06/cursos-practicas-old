

def pares(dimension):
	i=1
	pares=0
	while i<=dimension:
		if i % 2==0:

			print(i,end=" ")
		
		if i % 2==0:
			pares=pares+1
		


		if i==dimension:
			print("\n\n La cantidad de pares son " + str(pares))
			break;#Sale del flujo de ejecución del ciclo 
		#Incrementar contador en el ciclo	
		i=i+1				


rango=int(input("\n\n Ingrese hasta donde quiere saber los números pares  >"))
#Llamar a la función 

#Llamar al método 
print( pares(rango))


