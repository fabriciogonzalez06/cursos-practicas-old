#Crear un vector con frutas 
frutas=["Manzana","Pera","Sandia"]

#Añadir dos frutas mas con append y mostrar todo
frutas.append("Mango")
frutas.append("Melón")
print(frutas[:])

#Insertar en el índice 3 y 4 (insert) dos frutas más y mostrar nuevo vector 
frutas.insert(3,"Ciruela")
frutas.insert(4,"Melocotón")
print(frutas[:])

#Agregar varios elementos a la lista(extend) y mostrar 
frutas.extend(["Fresa","Marañon","Uva"])
print(frutas[:])

#Buscar índice de la fruta Mango y almacenar ese índice en una variable y mostrarlo 
indiceMango=frutas.index("Mango")
print(frutas[indiceMango])

#Verificar si existe Sandia en el arreglo de lo contrario mostrar un mensaje 
verificar="Sandia" in frutas
if(verificar==True):
	posFruta=frutas.index("Sandia")
	print("La fruta si se encuentra y esta en la posición",posFruta," ", frutas[posFruta])
	print(frutas[:])
else:
	print("La fruta no se encuentra")


#Quitar Pera de el vector y mostrarlo 
frutas.remove("Pera")
print(frutas[:])	

#Remover el ultimo elemento del arreglo y mostrar el arreglo 
frutas.pop()
print(frutas[:])


#Mostrar todos los elementos desde la posición del indice 3 
print(frutas[3:])

#Mostrar todos los elementos desde 0 hasta la poción 5 
print(frutas[0:5])
#Mostrar todos los elementos hasta la poción de indice 5
print(frutas[:5])

#Mostrar los elementos desde el indice 3 hasta el 6
print(frutas[3:6])

#Mostrar los elementos con indice negativo hacia la derecha 
print(frutas[:-4])

#Mostrar los elementos con indice negativo hacia la izquierda
print(frutas[-2:])

#Crear dos vectores y concatenarlo con un tercer vector 
paises1=["Mexico","Guatemala","Belice","Honduras","Francia"]
paises2=["Holanda","Canada","Puerto Rico","Brazil","Argentina"]
paisesUnidos=paises1+paises2
print(paisesUnidos[:])

#Extender a paises dos mas paises 
paisesUnidos.extend(["España","Portugal","Italia"])
print(paisesUnidos[:])