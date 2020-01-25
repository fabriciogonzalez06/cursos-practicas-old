nombres1=["Jorge","María","Alberto"]
nombres2=["Jose","Marcos","Juan"]
#Concatenar las dos listas anteriores en una tercera lista
nombresFinales=nombres1+nombres2
print(nombresFinales[:])
print("El Indice de Marcos es ",nombresFinales.index("Marcos"))

#Repetir listas con Repetidor * 
pares=[2,4,6,8]
print(pares[:])
pares.extend([10,12]*2)#Duplica los elementos 10 y 12 dos veces 
print(pares[:])