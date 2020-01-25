#Importar la librería 
from io import open 

#Abrir en modo escritura 
archivo=open("archivo.txt","w")
archivo.write("hola mucho gusto \n como estas? \n qué haces?")
archivo.close()

#abrir en modo lectura 
archivoLectura=open("archivo.txt","r")
#leer=archivoLectura.read()
#archivoLectura.close()
print(archivoLectura.read())
#utilizar seek para poner el cursor al inicio nuevamente del archivo de texto 
archivoLectura.seek(0)
print(archivoLectura.read())

#Aqui pone el puntero en el caracter 11
archivoLectura.seek(11)
print(archivoLectura.read())


#tambien read() tiene una cualidad que se le puede pasar como parámetro hasta donde quiere que se leea mandando un parametro 
archivoLectura.seek(0)
print(archivoLectura.read(15))#Lee hasta la línea 15

print("\n" + archivoLectura.read())#Imprime de la 11 en delante

#Posicionar el puntero en la mitad del archivo 
archivoLectura.seek(len(archivoLectura.read())/2)
#Imprimir la mitad 
print(" \n\n " + archivoLectura.read())
