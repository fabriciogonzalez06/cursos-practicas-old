#Uso del continue en un ciclo 
nombre="Angel Fabricio González"

contador=0

for i in nombre:

	if i==" ":
		continue#El continue omite el resto de código desde que se aplica 

	contador+=1

print("\n La cantidad de letras de " + nombre + " son: " + str(contador))		
