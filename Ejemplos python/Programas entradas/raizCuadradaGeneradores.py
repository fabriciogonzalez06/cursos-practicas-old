#Importar a clase para funciones matemáticas 
import math


def generarRaiz(inicio,fin):

	#ciclo while 
	while inicio<=fin:#Mientras 
		yield math.sqrt(inicio)

		#Incrementar contador 
		inicio+=1


#Programa Principal
inicio=0
final=0
recibeRaiz=0

#Pedir donde se comenzá a pedir la raiz cuadrada
inicio=int(input("\n Ingrese desde donde quiere comenzar a saber la raiz cuadra de los números >"))
#Validar variable 
while inicio<=0:
	print("\n Error, valor no válido, Ingrese nuevamente por favor  ")
	inicio=int(input("\n Ingrese desde donde quiere comenzar a saber la raiz cuadra de los números >"))

#Pedir el final de donde terminará de pedir los 
final=int(input("Ingrese hasta donde desea saber la raiz cuadrada de los números >"))
#validar que no sea menor que el rango inicial 
while final<inicio:
	print("\n Error, el final no puede ser menor que el rango de inicio, Ingrese nuevamente por favor ")	
	final=int(input("Ingrese hasta donde desea saber la raiz cuadrada de los números >"))

#crear objeto que recibira las raices 
raices=generarRaiz(inicio,final)
#mostrar los resultados llamando a una función 

res=1
while res==1 and inicio<=final:
	if res==1:
		print("\n La raíz cuadrada de " + str(inicio) + " es " + str(next(raices)))

	#preguntar si quiere ver otra raíz cuadrada 
	res=int(input("\n Desea saber otra raíz 1)Si 2)No   >"))
	#Validar respuesta 
	while res<1 or res>2:
		pritn("\n opción no valida, Ingrese nuevamente ")
		res=int(input("\n Desea saber otra raíz 1)Si 2)No   >"))

	inicio+=1


