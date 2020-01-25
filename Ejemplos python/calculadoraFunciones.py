#Función para calcular la operación a realizar 
def operacion(n1,n2,opc):
	if(opc==1):
		return n1+n2
	else:
		if (opc==2):
			return	n1-n2
		else:	
			if(opc==3) :
				return n1*n2
			else:
				if(opc==4) :
					if (n2==0):
						return "La División entre cero no esta definida"
					else:
						return n1/n2	
				else:
					return "La opción ingresada no es válida "	

			         	
		      		

#Crear variables y leeras 
#1)Suma 2)Resta 3)Multiplicación 4)División
#Llamar a funcipon operación y realizar la operación a realizar 
print(operacion(3,3,1))#Suma
print(operacion(10,3,2))#Resta
print(operacion(5,5,3))#Multiplicación
print(operacion(4,2,4))#División
print(operacion(2,0,4))#Error División entre cero 
print(operacion(2,4,6))#Error opción de operación no válida 
#Mandando variables con valores 
numero1=40
numero2=50
print(operacion(numero1,numero2,2))#Resta
#con variable para la opcion 
opcion=4
print(operacion(numero1,numero2,opcion))
						
					
			