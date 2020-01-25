#Llamamos al modulo de operaciones básicas 
import operaciones_mate_basicas 

#ahora para utilizar sus metodos tenemos que recurrir a la nomenclatura del punto 


#Pedir opción 
while ValueError:

	try:
		while True:

			n1=int(input("\n Ingrese el número 1 >"))
			n2=int(input("\n Ingrese el número 2 >"))
			operaciones_mate_basicas.menu()
			opc=int(input("\n Elija una opción >"))
			#Validar opción 
			while opc<1 or opc>5:
				print("\n Opción no válida ingrese nuevamente ")
				opc=int(input("\n Elija una opción >"))

			if opc==1:
				operaciones_mate_basicas.suma(n1,n2)	
			elif opc==2:
				operaciones_mate_basicas.resta(n1,n2)
			elif opc==3:
				operaciones_mate_basicas.multiplicacion(n1,n2)
			elif opc==4:
				##verificar que el dos no sea cero 
				if operaciones_mate_basicas.verificar(n2)==0:
					print("Error la división entre cero no esta definida ")
				else:
					operaciones_mate_basicas.dividir(n1,n2)	
			elif opc==5:
				break	

			
			continuar=int(input("\n Desea hacer otra operación 1)Si 2)No  >"))
			if continuar==2:
				break

	except ValueError:
		print("\n Se esperaba un número ")

	if opc==5:
		break	

	if continuar==2:
		break		