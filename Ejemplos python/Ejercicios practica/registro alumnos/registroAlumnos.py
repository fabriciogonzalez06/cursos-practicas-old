#Este programa registra diez alumnos y guarda la información en un archivo de texto que se pide al inicio el nombre y que deberá ingresar el maestro
#Importar las librerías necesarias 
from io import open 

#Crear metodo de escritura y lectura 

#Método solo para crear el arcivo 

def crear(nombre):

	archivo=open(nombre+".txt","w")
	archivo.close()

#Crear función de manipulacion de escritura y lectura 
def  Escritura(nombre,informacion):
	archivo=open(nombre+".txt","r+")#Se especifica que es de lectura y escritura 
	archivo.seek(len(archivo.read()))
	archivo.write(informacion)
	archivo.close()

#Método para mandar lo ocurrido a un archivo de texto 
def error(error):
	archivo=open("errores.txt","a+")
	archivo.write(error)
	archivo.close()


#Método para verificar la edad 
def verificarEdad(edad):
	ok=True
	#este metodo tiene un estado inicial verdadero si se llega a romper una regla pasa a estado falso y es lo que se devuelve
	edad2=int(edad)
	if edad.isdigit()==False:
		ok=False

	if 	edad2<10:
		ok=False

	if edad2>100:
		ok=False	

	return ok	

try:
	#Pedir el nombre de la materia 
	materia=input("\n Ingrese el nombre de la materia >")
	while  materia.isdigit()==True:
		print("\n Error no se permiten números como nombre, por favor ingrese nuevamente ")
		materia=input("\n Ingrese el nombre de la materia ")
	
	#Crear el archivo con el nombre de la materia 
	crear(materia)

	for i in range(2):
		nombre=input("\n Ingrese el nombre del alumno " + str((i+1)) + "  >")

		#Verificar el nombre 
		while nombre.isdigit()==True:
			print("\n Error el nombre no debe ser  numérico ingrese nuevamente por favor ")
			nombre=input("\n Ingrese el nombre del alumno 1 >")

		edad=input("\n Ingrese la edad de " + nombre + " >")
		
		#Llamar al metodo para verificar edad 
		while verificarEdad(edad)==False:#si se rompe una regla se repite hasta que todo este correctamente 
			print("\n error, la edad no debe ser letras o tampoco puede ser menor que 10 ni mayor que 100, Ingrese nuevamente")
			edad=input("\n Ingrese la edad de " + nombre + " >")

		lugar=input("\n Ingrese el lugar de residencia >")

		#Guardar en el archivo de texto comp primer parámetro el nombre de la materia 
		Escritura(materia,"Nombre: " + nombre + " Edad: " + edad + " Residencia: " + lugar + "\n")


except ValueError:
	print("\n Upss algo anduvo mal ")
	error("Error, se esperaba un número" )

	

