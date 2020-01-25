#Importar la librería para utilizar los métodos de la clase math
import math 

print("Programa de calculo de raíz cuadrada")
numero=int(input("\n Intruduce un número por favor:  >"))

intentos=0

while numero<0:
	print("\n No se puede encontrar la ríz de un número negativo")

	if intentos==2:#Cuando intentos sea 2 se mostrará un mensaje y se saldrá del ciclo mediante el break
		print("\n Ha consumido demasiados intentos, El programa ha finalizado.")
		break;#Sale del ciclo

	numero=int(input("\n Intruduce un número por favor:  >"))
	if numero<0:#si el número es menor que 0 se incrementará intentos 
		intentos=intentos+1


if intentos<2:#Si los intentos fueron menorque dos se procederá a calcular la raíz cuadrada
	solucion=math.sqrt(numero)#en la variable solución se llama al método sqrt de la clase math y se envia el parámetro a sacar raíz cuadrada
	print("\n La raíz cuadrada de " + str(numero ) + " es " + str(solucion) )
