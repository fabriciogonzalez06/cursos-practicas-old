#importar clase para la raiz cuadradra 
import math 

def menu2():
	print("*                    5)Raíz cuadrada                       *")
	print("*                    6)Potencia                            *")
	print("*                    7)Salir                               *")
	print("************************************************************")


#metodo para sacar la raíz cuadrada 
def raiz(num):	
	if num<=0:
		print("\n La raíz cuadrada no es menor o igual a cero ")
	else:
		print("\n La raíz cuadrada de " + str(num) + " es " + str(math.sqrt(num)))	

#Método para la potencia 
def potencia(base,exponente):
	if base==0:
		print("\n La base nunca debe ser cero ")
	else:
		print("\n El resultado de " + str(base) + "^" + str(exponente) + " = " + str(base**exponente) )			


	