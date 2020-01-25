#Creación de la clase coche
class coche():
	#Definir las propiedades de está clase 
	largoChasis=250
	anchoChasis=120
	ruedas=4
	enMarcha=False

	#Definir métodos 
	#Sempre se usa los métodos para una clase 
	#La palabra self hace la misma función que un this y siempre se pone como parametro
	def arrancar(self):
		self.enMarcha=True

	def estado(self):
			if self.enMarcha:
				return "El coche está en marcha"
			else:
				return "El coche está parado"


#Programa principal 
#Intanciar un objeto de la clase coche 
miCoche=coche()

#Acceder a las propiedades y métodos de la clase coche 
print("El largo del coche es ",miCoche.largoChasis)
print("El coche tiene " ,miCoche.ruedas,"Ruedas")
#Prender el choche solo hay que llamar al método encender 
miCoche.arrancar()
#mostrar el estado del coche j
print("El coche esta ",miCoche.estado())
