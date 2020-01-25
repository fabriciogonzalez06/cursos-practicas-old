class coche():
	#Declarar constructor y las propiedades con su estado inicial 
	#El constructor siempre ira con la palabra reservada __init__
	def __init__(self):
		##Encapsular las propiedades esto se hace anteponiendo al nombre nos guines bajos asi __hola
		#para que su valor no pueda ser modificado desde fuera de la clase
		self.__largoChasis=250
		self.__anchoChasis=120
		self.__ruedas=4
		self.__enMarcha=False

	#Método arancar 
	def arrancar(self,arrancamos):
		self.__enMarcha=arrancamos

		if self.__enMarcha:
			return "El coche esta en marcha"
		else:
			return "El coche está varado"

	#método que informa el estado del coche
	def estado(self):
		print("\n El largo de chasis es ",self.__largoChasis," el ancho del chasis es ",self.__anchoChasis,
			"El coche tiene ", self.__ruedas,"ruedas")	



#Instanciar a la clase 
miCoche=coche()
#Llamar al método arrancar y hacerlo con un print porque returna una cadena
print(miCoche.arrancar(True))
#llamar al metodo estado de la clase coche 


#miCoche.__largoChasis=400 si se habilita está linea no va ha hacer ningun efecto porque esta encapsulado en la clase 


miCoche.estado()

