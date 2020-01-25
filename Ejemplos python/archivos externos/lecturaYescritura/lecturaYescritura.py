from io import open 

#Abrir en modo l escritura 
archivo=open("meses.txt","w")#Archivo de escritura y lectura 

#Añadir unas lines al archivo de texto 
archivo.write("enero \n febrero \n marzo \n abril  \n mayo \n junio")
archivo.close()

#lectura y escritura
archivo_lectura=open("meses.txt","r+")
#almacenar todo en una lista mediante el readlines
listaMeses=archivo_lectura.readlines()
#imprimir la lista 
print(listaMeses)

#modificar el mes de febrero 
listaMeses[1]="Febrero fue modificado \n"

archivo_lectura.seek(0)#poner el cursor en 0 o al inicio  sino continua desde lo que hay en el archivo de texto

archivo_lectura.writelines(listaMeses)#se escriben las lineas de la lista pide una lista por parametro 

#cerrar el archivo de texto
archivo_lectura.close()
