def opcion():
	print("****************************************************************************")
	print("*|                       >>>  1)Agregar <<<                               |*")
	print("*|                       >>>  2)Eliminar <<<                              |*")
	print("*|                       >>>  3)Ver lista <<<                             |*")
	print("*|                       >>>  4)Ver tamaño<<<                             |*")
	print("*|                       >>>  5)Insertar  <<<                             |*")
 
i=0
lista=["jorge"]
opc=0
elemento=""
continuar=1

while continuar==1:
	opcion()
	opc=int(input("\n Elija una opción  >"))
	#Validar que ingrese una opción valida
	while opc<1 or opc>5:
		print("\n opción no válida , Ingrese nuevamente")
		opc=int(input("\n Elija una opción  >"))

	#Agregar elemento 
	if opc==1:
		elemento=input("\n Ingrese el elemento:  >")
		while elemento in lista:
			print("El elemento ya existe ingrese nuevamente")
			elemento=input("\n Ingrese el elemento:  >")
        #Aquí agrega el elemento ya verificado que no se repita 
		lista.append(elemento)

	if opc==2:
 		elemento=input("\n Ingrese el elemento a borrar:  >")
 		verificar=elemento in lista
 		
 		while verificar==False:
 			print("\n El elemento a borrar no existe, ingrese un elemento que si exista")
 			elemento=input("\n Ingrese el elemento a borrar:  >")
 			verificar=elemento in lista

 		#Borra elemento 
 		lista.remove(elemento)	


	if opc==3:
 	 	print(lista)


	if opc==4:
 		print("\n La longitud de la lista es " + str(len(lista)))


	if opc==5:
 		posicion=int(input("\n Ingrese la posicion donde desea insertar elemento  >"))
 		while posicion>len(lista):
 			print("\n La posición a insertar es invalida ingrese nuevamente ")
 			posicion=int(input("\n Ingrese la posicion donde desea insertar elemento  >"))

 		elemento=input("\n Ingrese el elemento >")

 		#Insertar en lista 
 		lista.insert(posicion,elemento)	

	continuar=int(input("\n Desea realizar otra operación  1)Sí 2)No > "))
	while continuar<1 or continuar>2:
		continuar=int(input("\n Error opción no válida, ingrese nuevamente 1)Sí 2)No > "))	





 		
		






print(lista)