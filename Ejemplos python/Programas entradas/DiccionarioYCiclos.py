#Función para el menú 
def menu():
	print("************************************************************")
	print("|             1)Agregar registro                           |")
	print("|             2)Modificar registro                         |")
	print("|             3)Eliminar registro                          |")
	print("|             4)Ver diccionario                            |")
	print("************************************************************")

#Función para agregar elementos a un diccionario 
def agregarDiccionario(diccionario,clave,elemento):
	diccionario[clave]=elemento
	return diccionario

#Método para verificar clave 
def verificarKeyAgregar(diccionario,clave):
	valor=False
	for i in diccionario:
		if i==clave:
			valor=True

	return valor 	

#Función que verifica si una clave  esta para eliminarla 
def verificarKeyEliminar(diccionario,clave):
	valor=False 
	for i in diccionario:
		if i==clave:
			valor=True

	return valor 		



#Programa principal 
miDiccionario={"fabricio":"Hola",1:"Peru"}
opc=0
seguir=1
dato=""
tipoValor=0
clave=""
masEle=1
verificarClave=False 
i=""
tamanio=0
while seguir==1:

	#Mostrar menu 
	menu()

	opc=int(input("\n  Elija una opción  >"))
	#Validar opción 
	while opc<1 or opc>4:
		print("Error, opción no válida ingrese nuevamente por favor ")
		opc=int(input("\n  Elija una opción  >"))

	if opc==1:

		#Pedir registro a  agregar y verificar si la clave no existe y si existe mostrar un error 
		tipoValor=int(input("\n Qué tipo de valor ingresará  1)Caracteres 2)numérico >"))
		#Validar tipo de valor 
		while tipoValor<1 or tipoValor>2:
			print("\n error, esta opción no está disponible, ingrese nuevamente")
			#Llamar al metodo para verificar clave 
			tipoValor=int(input("\n Qué tipo de valor ingresará  1)Caracteres 2)numérico >"))

		if tipoValor==1:
			clave=input("\n Ingrese la clave para acceder ")#Se leee un valor cadena
			#Recorrer el diccionario para ver si la clave existe o no y dar un valor booleano llamando a la función 
			verificarClave=verificarKeyAgregar(miDiccionario,clave)
		elif tipoValor==2:
			clave=int(input("\n Ingrese la clave númerica >"))#Se lee un valor numérico entero
			#Llamar al método para verificar clave
			verificarClave=verificarKeyAgregar(miDiccionario,clave)


		#Si la clave existe mandar un mensaje y sino pedir datos para esa clave 
		if verificarClave:

			print("\n Error la clave ya existe \n ")
		else:	
			#Agregar elementos a esta clave
			while masEle==1:
				dato=input("\n Ingrese un dato para " + str(clave) + " >")
				#llamar a la función para agregar dato 
				agregarDiccionario(miDiccionario,clave,dato)

				#Preguntar si desea ingresar mas elementos 
				masEle=int(input("\n Desea ingresar más elementos para  " + str(clave) + " 1)Sí  2)No >"))
				#Validar respuesta
				while masEle<1 or masEle>2:
					print("\nError, opción no válida, ingrese nuevamente")
					masEle=int(input("\n Desea ingresar más elementos para  " +  str(clave) + " 1)Sí  2)No >"))

	elif opc==3:

		print("Elemento a modificar " + str(miDiccionario.keys()))
		#Pedir registro a  agregar y verificar si la clave no existe y si existe mostrar un error 
		tipoValor=int(input("\n Qué tipo de valor eliminará  1)Caracteres 2)numérico >"))
			#Validar tipo de valor 
		while tipoValor<1 or tipoValor>2:
			print("\n error, esta opción no está disponible, ingrese nuevamente")
			#Llamar al metodo para verificar clave 
			tipoValor=int(input("\n Qué tipo de valor Eliminará  1)Caracteres 2)numérico >"))

		if tipoValor==1:
			clave=input("\n Ingrese la clave para eliminar y us datos asociados  ")#Se leee un valor cadena
			verificarClave=verificarKeyEliminar(miDiccionario,clave)
		elif tipoValor==2:
			clave=input("\n Ingrese la clave para eliminar y us datos asociados  ")#Se leee un valor cadena
			verificarClave=verificarKeyEliminar(miDiccionario,clave)

		if verificarClave==False:
			print("\n Error, la clave no existe \n")
		else:
		
		#Borrar de el diccionario la clave ingresada 
		
		
			if len(miDiccionario)>0:
				del(miDiccionario[clave])
			else:
				print("No hay claves que borrar ")						









