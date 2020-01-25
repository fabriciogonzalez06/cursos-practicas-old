#Método para mostrar rutulo 
def rotulo():
	print("****************************************************************")
	print("*                                                              *")
	print("*                   -> PROMEDIO ALUMNO <-                      *")
	print("*                                                              *")
	print("****************************************************************")
#Definir función para calcular el promedio del alumno
def promedio(n1,n2,n3,n4):
	promedio=(n1+n2+n3+n4)/4
	return promedio
#Función para imprimir si esta reprobado y aprobado 
def observacion(prom):
	if(prom<65):
		return "Reprobado"
	else:
		return "Aprobado"

#Imprimir metodo rotulo 
rotulo()
#Lectura de las variables	
print(" Ingrese el nombre del alumno")
nombre=input()
print("Ingrese la nota 1 de "+ nombre)
nota1=float(input())#Recordar siempre convertir los tipos 
print("Ingrese la nota 2 de "+nombre)
nota2=float(input())
print("Ingrese la nota 3 de "+nombre)
nota3=float(input())
print("Ingrese la nota 4 de "+nombre)
nota4=float(input())
#Llamar a función para calcular promedio
print("El promedio de ", nombre," es ",promedio(nota1,nota2,nota3,nota4))
print("El alumno ",nombre,"Esta",observacion(promedio(nota1,nota2,nota3,nota4,)))








