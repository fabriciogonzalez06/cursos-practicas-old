#Para importar un metodo de un modulo que esta en un paquete es de la siguiente manera 
#from calculosMatematicos.operaciones_mate_basicas import menu

#Para importar todos los metodos de un modulo que esta en un paquete es de la siguiente manera 
from calculosMatematicos.operaciones_mate_basicas import *

while True:
	try:
		#Imprimir menu 
		menu()
		opc=int(input("\n Seleccione una opción >"))
		#Validar opción ingresada 
		while opc<1 or opc>5:
			print("\n Error opción no valida, Ingrese nuevamente ")
			opc=int(input("\n Seleccione una opción >"))

		#Si es la opción 5 salir del programa 
		if opc==5:
			print("\n\n Gracias por utilizar el programa!!")
			break#Instrucción para salir del ciclo 


		num1=float(input("\n Ingrese el número 1 >"))
		num2=float(input("\n Ingese el número 2  >"))

		#segun opc llamar a los metodos del modulo del paquete calculosMatematicos
		if opc==1:
			suma(num1,num2)
		elif opc==2:
			resta(num1,num2)
		elif opc==3:
			multiplicacion(num1,num2)
		elif opc==4:
			if verificar(num2)==0:
				print("\n Error la división entre cero no está definida ")
			else:
				dividir(num1,num2)					
	except ValueError:
		print("\n Se esperaba un valor numérico ")