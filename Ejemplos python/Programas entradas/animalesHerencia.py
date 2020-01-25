#Clase base 
class animales():

	#Definir constructor de la clase
	def __init__(self):
		self.color=""
		self.colorOjos=""
		self.edad=3
		self.estaZoologico=False
		self.nombre=""

	#Método para ver si esta en el zoologico 
	def veficicar(self,veficicar):
		self.veficicar=veficicar
		if self.veficicar:
			print("El animal si esta en el zoologico")
		else:
			print("El animal no se encuentra en el zoologico")	

	def estado(self):
		print("Nombre ",self.nombre,"\n color ",self.color,"\n color ojos ",self.colorOjos,"\n edad ",self.edad,)		
		
#clase perro que herede de animales 
class perro(animales):
	ladrar=False
	
	#Método ladrar 
	def ladrar(self,ladra):
		self.ladrar=ladra
		if self.ladrar:
			return "El perro esta ladrando "
		else:
		 	return "El perro no está ladrando "	


#crear objeto de la clase perro
miPerro=perro()
#llenar propiedades de el objeto miPerro de la clase perro
miPerro.nombre="Max"
miPerro.color="blanco"
miPerro.colorOjos="azul"
miPerro.edad=3

miPerro.veficicar(True)

miPerro.estado()
print(miPerro.ladrar(False))