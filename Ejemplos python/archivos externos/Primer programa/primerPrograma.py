#Libreria para los manejos de archivos de texto 
from io import open 

#en archivo se guarda y crea el archivo t
archivo=open("archivo.txt","w")

frase="Hoy es un buen día para programar en python \n claro que siempre"

#EScribir en archivo 
archivo.write(frase)

#Cerrar archivo 
archivo.close()

#Archivo de lectura 
archivo1=open("archivo.txt","r")
#leer en una variable lo que tiene el archivo 
lectura=archivo1.read()
#leer con readlines y crea una lista 
#lista=archivo1.readlines()
#Cerrar el archivo 
archivo.close()
#Imprimir lo leido 
print(lectura)
#print(lista)

#para sobreescribir en el archivo
archivo3=open("archivo.txt","a")

archivo3.write("\n y nunca dejara de serlo")

archivo3.close()