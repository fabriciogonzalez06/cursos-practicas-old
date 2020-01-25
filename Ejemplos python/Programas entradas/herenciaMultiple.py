#Crear la clase padre 
class personas():

	#Crear constructor de la clase personas 
	def __init__(self):
		self.nombre=""
		self.apellido=""
		self.edad=0
		self.direccion=""
		self.correo=""

	#Método para ver si la persona es reciente 
	reciente=0
	def reciente(self,aniosTrabajo):
		self.reciente=aniosTrabajo
		if self.reciente>0 and self.reciente<3:
			return  "\n" + self.nombre + " si es reciente"	
		elif self.reciente>2:
			return  "\n" + self.nombre + " No es recinte"	

#Definir la clase empleado 
class empleado(personas):
	
	#Constructor de esta clase 
	def __init__(self):
		self.dni=""

	#Método para imprimir la información del empleado 
	def imprimirEmpleado(self):
		print("\n Nombre " + str(self.nombre) + "\n Apellido " + str(self.apellido) + "\n DNI "+ str(self.dni)+"\n Edad " + str(self.edad) +
				"\n Dirección " + str(self.direccion) + "\nCorreo " + str(self.correo)
			)	

#Clase empleado administrativo 	
class empleadoAdministrativo(empleado,personas): 
	pass

#Crear el objeto para la clase empleado 
empleado1=empleado()
aniosTra=0	

while True:
	try:
		#Asignar propiedades al objeto empledo1
		empleado1.nombre=input("\nIngrese el nombre del empleado >")
		empleado1.apellido=input("\n Ingrese el ap ellido de " + str(empleado1.nombre) + " >")
		empleado1.dni=input("\n Ingrese la dni de " + str(empleado1.nombre + " >"))
		empleado1.edad=int(input("\n Ingrese la edad de " + str(empleado1.nombre)+ " >"))
		empleado1.direccion=input("\nIngrese la direccion de " + str(empleado1.nombre)+ " >")
		empleado1.correo=input("\n ingrese el correo de " + str(empleado1.nombre)+ " >")
		while  ("." and "@" in str(empleado1.correo))==False:
			print("\n Correo inválido, ingrese nuevamente ")
			empleado1.correo=input("\n ingrese el correo de " + str(empleado1.nombre)+ " >")
		
		#LLamar al metodo reciente
		aniosTra=int(input("\n Ingrese los años de trabajo de " + str(empleado1.nombre) + " >"))
		print(empleado1.reciente(aniosTra))
		#Llamar al método que imprime toda la iformacion del empleado
		empleado1.imprimirEmpleado()

		##Si todo esta bien se sale del ciclo  
		break

	
	except ValueError:
		print("\n Se esperaba un número entero")

print("\n\n\n")

#Crear objeto del empleado amdinistrativo 
empleadAdmi=empleadoAdministrativo()
empleadAdmi.nombre="Juan"
empleadAdmi.apellido="Jimenez"
empleadAdmi.dni="33"
empleadAdmi.edad=12
empleadAdmi.direccion="Ojojona"
empleadAdmi.correo="adfa"
print(empleadAdmi.reciente(4))
