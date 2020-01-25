class coche():
	def desplazamiento(self):
		print("Me desplazo utilizando cuatro ruedas")

class moto():
	def desplazamiento(self):
		print("Me despazo utilizando dos ruedas")

class camion():
	def desplazamiento(self):
		print("Me despazo utilizando seis ruedas")	

#definir un método con el cual se utilizará el polimorfismo 
def desplazamientoVehiculo(vehiculo):
	vehiculo.desplazamiento()


#Crear el objeto de las clases 
Micoche=coche()
Mimoto=moto()
Micamion=camion()

#Utilizar el polimorfismo llamando al metodo donde surge y mandando el objeto de cualquier clase como parametro 
desplazamientoVehiculo(Micoche)	
desplazamientoVehiculo(Mimoto)
desplazamientoVehiculo(Micamion)					