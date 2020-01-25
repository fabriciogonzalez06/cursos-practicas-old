import calendar 

while True:

	anio=int(input("\nIngrese el año  >"))
	while anio<1930 or anio>2050:
		print("\n El año no es válido, Ingrese nuevamente ")
		anio=int(input("Ingrese el año  >"))

	mes=int(input("\n Ingrese el mes del 1 al 12 >"))
	while mes<1 or mes>12:
		print("El mes ingresado es incorrecto, ingrese nuevamente ")
		mes=int(input("\n Ingrese el mes del 1 al 12 >"))

	print("  ")
	#Mostrar calendario 
	print(calendar.month(anio,mes))	

	opc=int(input("\n otro mes? 1)Si 2)no "))
	while opc<0 or opc>2:
		print("\n Error opcion no valida ")
		opc=int(input("\n otro mes? 1)Si 2)no "))

	if opc==2:
		break	
