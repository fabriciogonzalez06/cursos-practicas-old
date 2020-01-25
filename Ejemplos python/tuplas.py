#Crear tupla, se hace con parentesis y no con conchetes }
miTupla=("Juan",12,43,True,"María")
#Acceder a un elemento de la tupla, es de la misma manera que con las listas
print(miTupla[3])

#Convertir una tupla en una lista con (LIST)
aniosTupla=(2001,2002,2003,2004,2005,2006)#Esto es una tupla 
anioslista=list(aniosTupla)#Convertir una tupla en una lista 
print(anioslista)#Con o sin corchetes[:] muestra toda la lista 

#Convertir una lista en una tupla (TUPLE)
listaDepartamentos=["Tegucigalpa","San Pedro Sula","Gracias a Dios","Tegucigalpa"]
tuplaDepartamentos=tuple(listaDepartamentos)#Convertir una lista en una tupla 
print(tuplaDepartamentos)#Al igual que las listas de puede imprimir solo el nombre de la tupla o también con corchetes[:] y sale toda la tupla

#Verificar si un elemento se encuentra en la tupla con método IN 
print("Gracias a Dios" in tuplaDepartamentos)
#Otra manera 
Verificar="Tegucigalpa" in tuplaDepartamentos
if(Verificar==True):
	print("El departamento sí se encuentra en la tuplaDepartamentos")

#Contar las veces que se encuentra un elemento en una tupla (COUNT)
print(tuplaDepartamentos.count("Tegucigalpa"))

#Ejemplo de departamentos con variables 
edades=(40,55,55,20,20,20,50,14,53,24,34,34)
edadBuscar=20
print("Se encuentra la edad",edadBuscar,edadBuscar in edades)#Verifica si se encuentra el contenido de la variable edadBuscar en edades
print(edades.count(edadBuscar))#Cuenta cuantas veces aparece el contenido de edadBuscar en la tupla edades

#Imprimir la longitud de una tupla con el método (LEN)
print("La longitud de la tupla es ", len(edades),"elementos")


#Tupla unitaria 
tuplaUnitaria=("Jose",)#Asi se define una tupla unitaria dejando la coma así
print("La longitud de la tupla unitaria es ",len(tuplaUnitaria))
