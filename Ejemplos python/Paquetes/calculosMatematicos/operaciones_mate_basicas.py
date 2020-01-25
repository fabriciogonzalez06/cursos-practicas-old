#Menu de operaciones 
def menu():
	print("************************************************************")
	print("*                                                          *")
	print("*               ELIJA UNA OPCIÓN                           *")
	print("*                    1)Suma                                *")
	print("*                    2)Resta                               *")
	print("*                    3)Multiplicación                      *")
	print("*                    4)División                            *")
	print("*                    5)Salir                               *")
	print("************************************************************")

def suma(n1,n2):
	print("\nLa suma de " + str(n1) + " + " + str(n2) + " = ", (n1+n2))


def resta(n1,n2):
	print("\nLa resta de "+ str(n1) + " - " + str(n2) + " = ", (n1-n2) )	

def multiplicacion(n1,n2):
	print("\nLa multiplicación de "+ str(n1) + " * " + str(n2) + " = ", (n1*n2))	

#Método para verificar si no ingresa un cero como segundo método para la division 
def verificar(n2):
	if n2==0:
		return 0
	else:
		return	1

#Método de la división 
def dividir(n1,n2):
	print("\nLa división de "+ str(n1) + " / " + str(n2) + " = ", (n1/n2))				