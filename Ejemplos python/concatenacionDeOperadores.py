#concatenación de operadores en python

print("Ingrese una edad")
edad=int(input())

if 0<edad<100:
	print("Edad correcta")#Si 0 es menor que la edad y la edad es menor que 100 la edad es correcta
	#sino pasa a edad incorrecta, se evalua de izquierda a derecha y si en dado caso no se cumple omite lo démas y pasa al else según sea el caso
else:
	print("Edad incorrecta")


print("")
#Vefificar los salarios 
salario_presidente=int(input("Ingrese el salario del presidente >"))
print("El salario del presidente es " + str(salario_presidente)+ "\n")

salario_director=int(input("Ingrese el salario del director >"))
print("El salario del director es " + str(salario_director)+ "\n")

salario_jefe_area=int(input("Ingrese el salario del jefe de area >"))
print("El salario del jefe area es " + str(salario_jefe_area)+ "\n")

salario_administrativo=int(input("Ingrese el salario del administrativo  >"))
print("El salario del administrativo es " + str(salario_administrativo)+ "\n")

#Uso de operadores concatenados
if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
	print("Todo anda bien en los salarios ")
else:
	print("Algo anda mal en los salarios")
