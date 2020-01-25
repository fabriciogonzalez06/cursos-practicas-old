#Vamos a hacer un ejemplo de un generador que devuelve los sub elementos de un elemento 
def devuleve_ciudades(*ciudades):#El asterisco le indica a la función que se pasarán un número indeterminado de parámetros 
	
	for elemento in ciudades:#Aquí elemento recorrera lo que se mande de ciudades
		
		for subElemento in elemento:#Aquí sub elemento recorrerá 1 a 1 cada elemento del elemento correspondiente si es una palabra cada letra la leerá de elemento
			
			yield subElemento#Aquí retorna el sub elemento en caso de que el elemento sea una palabra retorna cada letra 


	

#Llamar a la función y crear un objeto para recibir cada elemento devuelto por el yield
ciudades_devueltas=devuleve_ciudades("Tegucigalpa","Comayagua","Olancho")

#Llamar al elemento con next 
print(next(ciudades_devueltas))

#Otra vez 
print(next(ciudades_devueltas))

#otra vez
print(next(ciudades_devueltas))




#Ejemplo de un generador utilizando un yield from 
def devuelve_ciudades2(*ciudades):

	for elemento in ciudades:

		yield from  elemento


#Llamar a la función y crear un objeto para recibir cada elemento devuelto por el yield from 
ciudades_devueltas2=devuelve_ciudades2("Tegucigalpa","Comayagua", "Olancho")

#Llamar al elemento con next 
print(next(devuelve_ciudades2))

#Llamar al elemento con next 
print(next(devuelve_ciudades2))

