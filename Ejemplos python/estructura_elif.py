print("Ingrese el número 1")
num1=float(input())
print("Ingrese el número 2")
num2=float(input())
prom=(num1+num2)/2
if prom>0 and prom<10:
	print("Mal promedio")
elif prom>9 and prom<40:
	print("Promedio mal")
elif prom>39 and prom<65:
	print("Promedio muy bajo")
elif prom>64 and prom<100:
	print("Exelente promedio")


if prom>0 and prom<100:
	print("El promedio es mayor que 0 y menor que 100")
elif prom<=0:
	print("El promedio es negativo")
elif prom>=100:
	print("El promedio es mayor o igual que 100")





