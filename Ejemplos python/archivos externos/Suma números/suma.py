from io import open

#Métodos para controlar los archivos externos 
def escribir(cadena):
	#Crear el archivo
	archivo=open("operaciones.txt","w")
	#manipularlo 
	archivo.write(cadena)
	#Cerrar el archivo 
	archivo.close()

def leerArchivo():
	archivo=open("operaciones.txt","r")
	#leer de la ruta especifica 
	lectura=archivo.read()
	archivo.close()
	return lectura

def sobreEscribir(cadena):	
	archivo=open("operaciones.txt","a")

	#sobreEscribir en el archivo 
	archivo.write("\n" + cadena)
	archivo.close()

print(leerArchivo())

while True:
	try:
		nombre=input("\n Ingrese su nombre >")
		sobreEscribir(nombre)

		while True:
			num1=float(input("\n Ingrese el número 1 >"))
			sobreEscribir(str(num1))
			num2=float(input("\n Ingrese el número 2 >"))
			sobreEscribir(str(num2))
			res=num1+num2
			sobreEscribir(str(res))
			

			print("\n El resultado de la suma es " + str(res))

			opc=int(input("\n más sumas para " + nombre + "?  1)si 2)no   >"))
			while opc>2 or opc<1:
				print("\n Error, opción no valida ingrese nuevamente ")
				opc=int(input("\n más sumas para " + nombre + "?  1)si 2)no   >"))

			if opc==2:
				break #Salir si opc es igual a dos 	

		opcnom=int(input("\n Más nombres? 1)si 2)no  >" ))
		while opcnom<1 or opcnom>2:
			print("\n Opción no valida ingrese de nuevo  ")	
			opcnom=int(input("\n Más nombres? 1)si 2)no  >" ))

		if opcnom==2:
			break		


	except ValueError:
		print("\n Se esperaba un número")
		


