print("1)Ha minusculas 2)Ha mayusculas ")
opc=int(input("\n Ingrese la opción a convertir >"))
if opc==1:
	cadena=input("\n Ingrese la cadena a convertir >")
	print("\n La cadena a convertir es "+cadena + " = " +cadena.lower())#Aquí convierte  minusculas 
elif opc==2:
	cadena=input("\n Ingrese la cadena a convertir >")	
	print("\n La cadena a convertir es "+cadena + " = " + cadena.upper())#Aquí solo convierte a mayusculas 
	#más el metodo mostrando en pantalla lo que hay en esa variable

#Otro método 
def convertirMayus(cadena):
	convertido=cadena.upper()
	return convertido

def convertirMinus(cadena):	
	convertido=cadena.lower()
	return convertido


print("1)A minusculas 2)A mayusculas \n")
opc=int(input("\n Ingrese una opción >"))
if opc==1:
	cadena=input("\n Ingrese la cadena a convetir ")
	print("\n " + cadena + " = " + convertirMinus(cadena))
elif opc==2:
	cadena=input("\n Ingrese la cadena a convertir ")
	print("\n " + cadena + " = " + convertirMayus(cadena))	


