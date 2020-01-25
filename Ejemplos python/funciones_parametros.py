#Función para la suma con parametros
def suma(n1,n2):
	return n1+n2
#Llamar a la función suma e imprimir su valor 
print(suma(2,5.3))
print(suma(3.55,-1))
#ejemplo dos funciones con parámetros 
def suma2(a,b):
	resultado=a+b
	return resultado
#Llamar a la función e imprimir su resultado de dos variables con valores
num1=2
num2=4 	
print("El resultado de  ",num1,"  + ",num2," es ",suma2(num1,num2))
#Función para calcular una división 
def division(n1,n2):
	if n2==0:
		return "Error, la división entres cero no esta definida "
	else:
		return n1/n2
#Llamar a la función y definir dos variables para enviarle como parámetro
num1=6
num2=0
print("El resultado de " , num1 ," /", num2, " es ",division(num1,num2) )			