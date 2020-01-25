#importar la libreria
import pickle 

#Crear instancia del metodo para io 
archivo=open("lista","rb")

#REscatar con el metodo load de la clase pickle 
rescatado=pickle.load(archivo)

print(rescatado)

archivo.close()

for i in rescatado:
	print(i)


print("tamaño " + str(len(rescatado)))
print("Index de True " + str(rescatado.index("True")))

rescatado.remove("True")

print(rescatado)


