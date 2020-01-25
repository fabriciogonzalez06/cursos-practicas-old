#El manejo de excepciones ocurre cuando la sintaxis del programa esta todo bien pero hay errores que no son permitios por ejemplo
#La división entre cero o que se espere un valor entero y se reciba uno decimal o que se espere un valor entero y se reciba
#un valor tipo cadena 

def suma(n1,n2):
	return n1+n2

def resta(n1,n2):
	return n1-n2

def multiplicacion(n1,n2):
	return n1*n2

def division(n1,n2):
	try:
		return n1/n2
	except ZeroDivisionError:
		print("No se puede dividir entre cero")
		return "Operación Errónea"	


numero1=0
numero2=0
opc=0
continuar=1

    	  

	

while True:

	while True:
		try:
			numero1=float(input("\n Ingrese el número 1   :   >" ))
			numero2=float(input("\n Ingrese el número 2   :   >"))
			break
		except ValueError:
   			print("Error se esperaba un valor numérico ingrese nuevamente")


	while True:
		try:
			opc=int(input("\n Ingrese la operación a realizar 1)Suma 2)Resta 3)multiplicacion  4)División "))
   			
			break
		except ValueError:
			print("Se esperaba un número entero Ingrese nuevamente")	



	if opc==1:
		print(suma(numero1,numero2))
	elif opc==2:
		print(resta(numero1,numero2))
	elif opc==3:
		print(multiplicacion(numero1,numero2))
	elif opc==4:
		print(division(numero1,numero2))
	else:
		print("opción no valida ")

	while True:
		try:
			continuar=int(input("Otra operación 1)Sí 2)No  >"))	
			#si ingresa un valor correcto se sale de este while 
			break	
		except ValueError:
			print("se esperaba un entero ")

	#Salir del ciclo principal si cumple la condición
	if continuar==2:
		break



		




