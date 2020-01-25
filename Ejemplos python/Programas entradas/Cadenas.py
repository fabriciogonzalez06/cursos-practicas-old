#Prueba con cadenas 
while True:
	
	nombreUsuario=input("\nIntroduce tu nombre de usuario >")
	
	while nombreUsuario.isalpha()==False:
		print("\n debe ingresar una cadena ")
		nombreUsuario=input("\nIntroduce tu nombre de usuario >")

	#Mostrar opciones de cadenas 	
	print("\n El nombre es " + nombreUsuario.upper())#Convierte todo a mayuscula 
	print("\n El nombre es " + nombreUsuario.lower())#Convierte todo a minuscula 
	print("\n El nombre es " + nombreUsuario.capitalize())#Convierte la primer letra en mayuscula no importa si todas estan en mayuscula o minuscula
	#count devuelve el número de veces que se encuentra una letra o valor en una cadena tambien se puede poner el valor inicial y final de busqueda
	print("\n La letra a aparece  " + str(nombreUsuario.count("a",1,55  )) + " Veces en el nombre " + nombreUsuario)
	#print("\n El nombre es " + nombreUsuario.encode("a"))
	print("\n El nombre contiene una F  en el índice " + str(nombreUsuario.find("f")) + " De fabricio")#Devuleve el indice donde se encuentra la letra primera 
	#Index es igual que find a diferencia que si no encuentra nada lanza un error de valor ValueError
	print("\n El nombre contiene una F en el indice  " + str(nombreUsuario.index("f")))
	print("\n El nombre es " + nombreUsuario.replace("a","j"))#remplaza la a por la j 

	continuar=input("Más operaciones 1)si 2)no >")

	while continuar.isdigit()==False :
		print("Ingrese un digito ")
		continuar=input("Más operaciones 1)si 2)no >")
		

	if int(continuar)==2:
		break
				
		

		
	
	