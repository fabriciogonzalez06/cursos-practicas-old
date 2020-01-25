#Clase padre 
class vehiculos():

	#crear contructor 
	def __init__(self,marca,modelo):
		#Estado inicial de las propiedades de la clase padre
		self.marca=marca
		self.modelo=modelo
		self.enMarcha=False
		self.acelera=False
		self.frena=False

	#Método para arrancar 
	def arrancar(self):
		self.emMarcha=True

	#Método para acelerar 
	def acelerar(self):
		self.acelera=True

	#Método para frenar
	def frenar(self):
		self.frena=True

	#Método para mostrar el estado 
	def estado(self):
		print("Marca ",self.marca,"\n Modelo: ",self.modelo,"\n En marcha ",self.enMarcha,"\n acelerar ",self.acelera," \n Frenar ",self.frena)	

#Crear una clase que herede de la clase vehiculos 
class moto(vehiculos):
	pass


#Crear instancia de la clase moto 
miMoto=moto("honda","cbr");#Se mandan estos parámetros al contructor que los requiere

miMoto.estado();				
