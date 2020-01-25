letras=("a","x","v","f","k","k","i","ll","l","p","a","b")#tupla 

#verificar si se encuentra la i en la tupla 
verificar="i" in letras
if(verificar==True) :
	print("La letra a buscar si se encuentra")
#Buscar su posición 
posicion=letras.index("i")
print("La posición de la letra es ",posicion)	
#Buscar el número de veces que aparece la letra en la tupla 
contar=letras.count("i")
print("Las veces que aparece la letra son ",contar)
#Buscar la longitud de la tupla 
longitudTupla=len(letras)
print("La longitud de la tupla es de ",longitudTupla,"Elementos")

#convertir la tupla en una lista 
letrasLista=list(letras)
print(letrasLista[:])
#Agregar elementos a la lista con append
letrasLista.append("j")
letrasLista.append("m")
letrasLista.append("n")
print(letrasLista)
#Insertar elementos a la lista con insert
letrasLista.insert(4,"j")
letrasLista.insert(2,"s")
letrasLista.insert(15,"k")
print(letrasLista[:])
#Agregar varios elementos a la lista con extend
letrasLista.extend(["h","k","p","o"])
print(letrasLista)
#Eliminar el ultimo elemento agredado de la lista con pop
letrasLista.pop()
print(letrasLista)
#Eliminar la letra  f de la lista 
letrasLista.remove("f")
print(letrasLista)

#verificar el tamaño de la lista 
print("El tamaño de la lista es de ", len(letrasLista),"Elementos")

#Verificar si se encuelra la letra k y cuantas veces 
buscarLetra="k"
busqueda=buscarLetra in letrasLista
if(busqueda==True):
	print("La letra ",buscarLetra,"Si se encuentra en la lista,",letrasLista.count(buscarLetra),"Veces")

#Convertir lista a tupla 
tuplaNueva=tuple(letrasLista)
print(tuplaNueva)

