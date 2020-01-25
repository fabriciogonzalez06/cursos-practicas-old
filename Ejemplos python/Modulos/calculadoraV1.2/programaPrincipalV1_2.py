#Versión 1.0 seria para importar el siguiente código 
#import operaciones_mate_basicas  
"""Siempre utilizando la nomenclatura del punto para acceder a los metodos de este modulo pero esto consume recursos entonces 
	Hay una forma mas optimizada de llamar a los métodos o variables y dejar de utilizar la nomenclatura del punto 
	y es la siguiente :
"""

from operaciones_mate_basicas import suma #Aquí solo importamos el método suma nada más 

#Probar 
suma(2,3)

from operaciones_mate_basicas import resta 

#Probar 
resta(3,-4)

from operaciones_mate_basicas import multiplicacion,verificar,dividir#Se puede importar varias 

multiplicacion(2,3)

if verificar(0)==1:

	dividir(2,4)
else:
	print("\n Error División entre cero")
