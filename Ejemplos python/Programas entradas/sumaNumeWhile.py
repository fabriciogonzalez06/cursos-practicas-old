#Programa que suma o acumula los números que va ingresando el usuario 

acumNum=0
contPares=0
contImpares=0
contNume=0
num=0
opc=""
opcMayus="SI"

while opcMayus=="SI":
	#Contar números
	contNume=contNume+1
	num=int(input("\n Ingrese un número > "))
	#validar que no ingrese números 0 
	while num==0:
		print("\n No se admiten 0, Ingrese nuevamente")
		num=int(input("\n Ingrese un número > "))
	
	#Acumular números 
	acumNum=acumNum+num
	if num%2==0:
		#contar pares
		contPares=contPares+1

	else:
		#contar impares
		contImpares=contImpares+1

	opc=input("\n Desea ingresar otro número? SI/NO >>>")
	opcMayus=opc.upper()		

print("\n Números ingresados " + str(contNume) + "\n\n Suma de los Números:  " + str(acumNum) + " \n\n Pares: " + str(contPares)  + " \n\n Impares: "+ str(contImpares))