#importar la libreria 
import pickle 

#Crear variable en modo lectura 
fichero=open("lista","wb")


lista=[]

for i in range(10):
	ingresar=input("\n Ingrese algo para la lista >")
	lista.append(ingresar)

#ingresar y empaquetar la lista 
pickle.dump(lista,fichero)	


#Cerrar fichero 
fichero.close()