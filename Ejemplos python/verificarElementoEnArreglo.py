colores=["Rojo","Verde","Amarillo"]
#Verificar si el coloer Verde se encuentra en la lista con esta función IN si se encuentra devuelve true y sino false 
print("Verde" in colores)#Devolvera un true porque sí se encuentra 
print("Rosado" in colores)#Devolverá False porque no se encuentra

#Python acepta todo tipo de datos en un arreglo o lista 
datos=[30,50.50,"Amarillo","Jorge",False,True]
print(datos[:])#Muestra matriz 
print(False in datos)#Devuelve  true

#Eleminar elemento de una lista (REMOVE)
datos.remove(30)#Remueve el 30 del vector 
print(datos[:]) 

#Eliminar el último elemento agregado a la lista con POP
datos.pop()
print(datos[:])#Elimina true de la lista 