import pickle

#Crear lista nombres 

nombres=["Ana","Pedro","Maria","José"]

#Crear fichero
ficheroBinario=open("listaNombres","wb")

#volcamiento con el pikle pide dos parámetros 
pickle.dump(nombres,ficheroBinario)

#Cerrar fichero 
ficheroBinario.close()

#ya volcado se puede hasta borrar 

del(ficheroBinario)