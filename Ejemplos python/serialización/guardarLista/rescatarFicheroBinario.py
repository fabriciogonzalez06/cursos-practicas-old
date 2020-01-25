#Importar librería 
import pickle 

archivo=open("listaNombres","rb")

lista=pickle.load(archivo)

archivo.close()
print(lista)