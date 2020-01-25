acum=0
notas=0
promedio=0
nombre=input("\n Ingrese el nombre del alumno > ")
for i in range(4):
	notas=float(input("Ingrese la nota " + str(i+1) +" de "+ nombre + " >"))
	acum=acum+notas

promedio=acum/4
print("\n El promedio de " + nombre + " es " + str(promedio))	



	