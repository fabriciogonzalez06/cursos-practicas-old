'''
Este es un comentario largo y esto es diccionarios 
Esta asociado a una clave y un valor o una clave y muchos valores 
'''
miDicionario={"Alemania":"Berlín","Fracia":"París","Reino Unido":"Londres","España":"Madrid"}#Esto es un diccionario con claves y valores
#Imprimir diccionario 
print(miDicionario)
#Imprimir un elemento del diccionario por medio de la clave
print(miDicionario["Alemania"])#Imprime el valor en este caso la capital 

#Agregar elementos a un diccionario 
miDicionario["Italia"]="lisboa"
print(miDicionario)

#Modificar un elemento del diccionario 
'''Se hace llamando al valor de la clave y se modifica su contenido, como no pueden haber dos claves con el mismo nombre dentro
de los diciionarios si se ingresa una clave ya existente lo que pasa es que se sobreescriben los datos 
que contenia por los modificados '''
miDicionario["Italia"]="Roma"
print(miDicionario)

#Eliminar un elemento del diccionario (Del)
del(miDicionario["Reino Unido"])
print(miDicionario)

#Los diccionarios las claves pueden ser de todo tipo al igual que sus valores 
Dic={5:"Jonas","cuatro":22,"Pasaporte":True}
print(Dic["Pasaporte"],Dic[5])

#Agregar una tupla al diccionario 
miTupla=("España","Francia","Reino Unido","Alemania")
miDicionario={miTupla[0]:"Madrid",miTupla[1]:"París",miTupla[2]:"Londres",miTupla[3]:"Berlín"}
print(miDicionario)
print(miDicionario[miTupla[2]])#Esto es una manera devuelve Londres
print(miDicionario["Reino Unido"])#Esta es otra manera siempre devolveera Londres


#Agregar una tupla de diferente manera 
datos={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","Anillos":(1991,1992,1993,1996,1997,1998)}
print(datos)
print(datos["Anillos"])#Imprime los elementos de la clave anillos

#Un diccionario dentro de otro diccionario 
datos={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","Anillos":{"Temporadas":(1991,1992,1993,1996,1997,1998)}}
print(datos["Anillos"])

#Imprimir las llaves de los diccionarios 
print(datos.keys())

#IMprimir los valores de las claves de los diccionarios 
print(datos.values())

#Imprimir la longitud de el diccionario
print(len(datos))





