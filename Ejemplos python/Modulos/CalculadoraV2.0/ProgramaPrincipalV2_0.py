#ahora importamos todos los métodos o clases de ese modulo 
from operaciones_mate_basicas import *
from operaciones_mate_intermedio import * 
#en este programa se hace uso de dos modulos 

while True:
	try:
		#Llamar al método menú 
		menu()
		opc=float(input("\n Elija una opción >"))
		#Verificar que la opción sea valida 
		while opc<1 or opc>7:
			print("\n La opción ingresada es inválida, ingrese nuevamente ")
			opc=float(input("\n Elija una opción >"))

		#Si la opción es 7 salir de primera 
		if opc==7:
			break	#Se sale del programa

		#Verificar el caso especial de la raiz cuadrada 
		if opc==5:
			num1=int(input("\n Ingrese el número a sacar raiz cuadrada >"))
			#Llamar al metodo raiz de el modulo operaciones_mate_intermedio
			raiz(num1)
		elif opc==6:
			num1=float(input("\n Ingrese la base  >"))
			num2=float(input("\n ingrese el exponente  >"))
			potencia(num1,num2)

		else:
			num1=float(input("\n Ingrese el número 1 >"))
			num2=float(input("\n ingrese el número 2 >"))
		

		#opciones de operaciones 
		if opc==1:
			suma(num1,num2)	
		elif opc==2:
			resta(num1,num2)
		elif opc==3:
			multiplicacion(num1,num2)
		elif opc==4:
			if verificar(num2)==0:
				print("\n La división entre cero no esta definida ")
			else:
				dividir(num1,num2)
	

		 				

	except ValueError:
		print("\n Se esperaba un valor númerico o si es raíz un valor entero \n ")

		
		
				



