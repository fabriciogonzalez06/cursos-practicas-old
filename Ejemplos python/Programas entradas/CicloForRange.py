#El range en el ciclo for cumple las veces que se va a repetir el ciclo for 
#Ejemplo
acumSuma=0
vueltas=int(input("Ingrese la cantidad de vueltas que quiere que de el ciclo >"))
for i in range(vueltas):
	num=int(input("Ingrese el número " + str(i + 1) + " >"))
	acumSuma=acumSuma + num

print("\n La suma de los números es " + str(acumSuma))	
