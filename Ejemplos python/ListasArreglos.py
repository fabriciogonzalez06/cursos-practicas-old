#Ejemplo listas o arreglos en python 
miLista=["Jorge","Jose","Marcos","Juana"]

#Imprimir lista completa 
print(miLista[:])
print("")
#Acceder a un elemento en concreto mediante la pocisión del índice 
print(miLista[2])
print("")
#Sí ponemos un índice negativo le da vuelta al conteo o empieza de la izquierda hacia la derecha 
autos=["Mercedez","Toyota","Corrolla","Ford","Hummer","Eclipse",]
print(autos[-2])
print(autos[-1])

#Acceder a una porción de la lista 

print(autos[0:3])#Accede desde la poción o hasta la pocisión 3-1 sería solo los primeros tres elemntos contando desde 0 
#También se puede de la siguiente manera y con los mismos resultados 
print(autos[:3])#Python sobrentiende que tiene que empezar desde el cero 

#También puedo imprimir entre rangos 
print(autos[1:5])

#También podemos acceder a los ultimos elementos de la siguiente manera 

diasSemana=["Lunes","Martes","Miercoles","Jueves","Viernes","Sábado","Domingo"]
print(diasSemana[3:])#Accede a los elementos desde el índice tres hasta el final 
