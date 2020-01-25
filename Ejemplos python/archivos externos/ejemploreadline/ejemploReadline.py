#IMportar librería 
from io import open

archivo=open("dias.txt","w")
archivo.write("lunes \n martes \n miercoles \n jueves \n viernes \n sabado \n domingo ")
archivo.close()

#Abrir en modo lectura 
modoLectura=open("dias.txt","r")
print(modoLectura.readline())#lee la primera linea 
print( "\n" + modoLectura.read())#Lee lo restante a partir del lunes 

#leer todas las lineas en una lista 
modoLectura.seek(0)
print("Modo lista \n " + str( modoLectura.readlines()))
modoLectura.close()