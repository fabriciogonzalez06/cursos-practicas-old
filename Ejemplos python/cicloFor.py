for i in [1,2,3,4,5,6,7,8,9,10]:
	lista=["hola"]
	print("1)Agregar 2)Buscar 3)eliminar 4)Ver lista 5)Ver tamaño")
	opc=int(input("\n Ingrese una opción a realizar >"))
	if opc==1:
		agregar=input("\n Ingrese una cadena a agregar >")
		lista.extend([agregar])
		print(lista)
	elif opc==2:
		buscar=input("\n Ingrese la cadena a buscar >")	
		verificar=buscar in lista
		if verificar==True:
			print(buscar + "Si se encuentra  y esta en la posición " + str(lista.index(buscar)))
		else:
			print(buscar + "No se encuentra ")
	elif opc==3:
		eliminar=input("\nIngrese la cadena a eliminar >")
		if eliminar in lista == True:
			lista.remove(eliminar)
		else:
			print("No existe el elemento")
	elif opc==4:
		print(lista[:])
	elif opc==5:
		print("El tamaño de la lista es " + str(len(lista)))				

			

	