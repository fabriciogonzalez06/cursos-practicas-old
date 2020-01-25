#Crear la clase empleados 
class Empleados():

	#Constructor de las propiedades 
	def  __init__(self):
		self.nombre=""
		self.apellido=""
		self.edad=0
		self.correo=""
		self.horasTrabajadas=0
		self.diasTrabajados=0
		self.pagoPorHora=0
		self.categoria=""
		self.descuento=0.0
		self.subt=0.0
		self.totalPagar=0.0

	#Método para calcular el subtotal a pagar 
	def subtotal(self):
		self.subt=self.horasTrabajadas*self.diasTrabajados*self.pagoPorHora
		return self.subt

	def descuentoADar(self):
			
		if self.categoria=="a" or self.categoria=="A":
			self.descuento=self.subtotal*0.30
		elif self.categoria=="b" or self.categoria=="B":
			self.descuento=self.subtotal*0.20
		elif self.categoria=="c" or self.categoria=="B":
			self.descuento=self.subtotal*0.10

	#metodo para imprimir la información 
	def imprimir(self):
		print("El nombre de empleado es " , self.nombre," ",self.apellido," La edad de ", self.nombre, "es ",sel.edad,
			"\n El correo electrónico de ",self.nombre, "es ",self.correo,"\n Las horas trabajadas ",self.horasTrabajadas, 
			"Los dias trabajados", self.diasTrabajados,"El pago por hora es ",self.pagoPorHora,"\n La categoria de ", self.nombre," ",self.categoria,
			"\n El subtotal a pagarle ",self.subtotal,"\n el bono por la categoria es ",self.descuento,
			"\n El total a pagarle a  ",self.nombre ,"es",self.totalPagar)					
				


		
#programa principal 
#crear instancia de la clase empleados 
empleado1=Empleados()

#pedir los datos del empleado 


try:
	empleado1.nombre=input("\n Ingrese el nombre del empleado  >")
	empleado1.apellido=input("\n Ingrese el apellido de " + empleado1.nombre + " >")

	#while para controlar los datos numéricos 

	while True:
		

		try:

			empleado1.edad=int(input("\n Ingrese la edad de " + empleado1.nombre + ">"))
			empleado1.correo=input("\n Ingrese el correo electrónico de " + empleado1.nombre + " " + empleado1.apellido + ">")
			empleado1.horasTrabajadas=int(input("\n Ingrese las horas trabajadas por día de " + empleado1.nombre + " >"))

			#Controlar error de horas incorrectas mayores de 8 y menores o iguales a cero
			while empleado1.horasTrabajadas<=0 or empleado1.horasTrabajadas>9:
				print("Error, las horas trabajadas son incorrectas, no mayor de 8 ni menor o igual a cero ")
				empleado1.horasTrabajadas=int(input("\n Ingrese las horas trabajadas por día de " + empleado1.nombre + ">"))
			
			empleado1.diasTrabajados=int(input("\n Ingrese los días trabajados al mes de " + empleado1.nombre + ">"))
			
			#Validar dias trabajados 
			while empleado1.diasTrabajados<=0 or empleado1.diasTrabajados>20:
				print("Error, los dias trabajados al mes no pueden ser mayor de 20 ni menor que 0, ingrese nuevamente ")
				empleado1.diasTrabajados=int(input("\n Ingrese los días trabajados al mes de " + empleado1.nombre + ">"))

			#Ingresar pago por hora 
			empleado1.pagoPorHora=float(input("\n Ingrese el pago por hora de " + empleado1.nombre + " >"))
			#Validar pago por hora 
			while empleado1.pagoPorHora<=0:
				print("Error, Pago por hora inválido ingrese nuevamente")
				empleado1.pagoPorHora=float(input("\n Ingrese el pago por hora de " + empleado1.nombre + " >"))


			empleado1.categoria=input("\n Ingrese la categoria del empleado a,b,c   >")
			#Validar categorioa 
			#while empleado1.categoria!="a" or 	empleado1.categoria!="A" or empleado1.categoria!="b" or empleado1.categoria!="B" or empleado1.categoria!="c" or empleado1.categoria!="C":

				
				#print("Error, categoria invalida ingrese nuevamente ")
				#empleado1.categoria=input("\n Ingrese la categoria del empleado a,b,c   >")



			#Calcular subtotal 
			empleado1.subtotal()

			#Calcular el descuento a dar 
			float(empleado1.descuentoADar())

			#Calcular función  que imprime todo 
			empleado1.imprimir()
			#Si todo esta bien se sale del ciclo 
			break


		except ValueError:
			print("Se esperaba un entero")
		except ValueError:
			print("Se esperaba una cadena")	
			

except ValueError:
	print("Se esperaba una cadena")
	
