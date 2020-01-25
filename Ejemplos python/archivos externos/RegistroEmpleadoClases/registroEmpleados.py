#Importar la librería necesaria 
from io import open 

#Crear clase para manipular los archivos de texto 
class manejoArchivos():
	
	#Crear método para escribir en un archivo de texto 
	def escribir(self,nombreArchivo,infor):
		archivo=open(nombreArchivo+".txt","a")
		archivo.write( infor + "\n")
		archivo.close()

	
	def lectura(self,nombreArchivo):
		archivo=open(nombreArchivo+".txt","r")
		leido=archivo.read()
		archivo.close()
		return leido


#Crear instancia de la clase 
archivo=manejoArchivos()

try:
	#Traer informacion de 
	traerNombre=input("Ingrese el nombre de quien desea traer la informacion  >")
	print(archivo.lectura(traerNombre))
except FileNotFoundError:
	print("Error, el archivo no existe")




nombre=input("\n Ingrese su nombre >")
archivo.escribir(nombre,"nombre: " + nombre)
apellido=input("\n Ingrese el apellido de " + nombre + " >")
archivo.escribir(nombre,"Apellido: " + apellido)
edad=int(input("\n Ingrese la edad de " + nombre + " >"))
archivo.escribir(nombre,"Edad: " + str(edad) )	
correo=input("\n Ingrese el correo electronico de " + nombre + " >")
archivo.escribir(nombre,"Correo Electrónico: " + correo)
