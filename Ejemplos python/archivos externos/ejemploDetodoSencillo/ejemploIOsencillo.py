#Importar la libreria
from io import open 

#modo write
archivo=open("archivo1.txt","w")
frase1="Hola que tal Fabricio?"
archivo.write(frase1)
archivo.close()

archivo1=open("archivo2.txt","w")
frase2="Hola esto es una prueba de python"
archivo1.write(frase2)
archivo1.close()

#Modo append
archivo=open("archivo1.txt","a")
frase="\n Espero tengas un buen dia"
archivo.write(frase)
archivo.close()

archivo1=open("archivo2.txt","a")
frase="\n Siempre será magnifico programar en python"
archivo1.write(frase)
archivo1.close()


#Lectura de los dos ejemplos
#Modo read 
archivo=open("archivo1.txt","r")
lectura1=archivo.read()
archivo.close()
print(lectura1)

archivo1=open("archivo2.txt","r")
lectura2=archivo1.read()
archivo1.close()
print(lectura2)

#modo readlines almacena una lista 
archivo=open("archivo1.txt","r")
lectura1=archivo.readlines()
archivo.close()
print(lectura1)


archivo1=open("archivo2.txt","r")
lectura2=archivo1.readlines()
archivo1.close()
print(lectura2)