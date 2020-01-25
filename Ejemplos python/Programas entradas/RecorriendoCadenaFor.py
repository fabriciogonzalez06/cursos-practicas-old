#Recorrer una cadena en python 
for i in "hola":
	print(i)#ESte código imprimirá en pantalla cada elemento de la cadena hola en este caso seria cada letra 

print("\n")
for i in "Que tal":
	print(i, end=" ")#aquí imprimira cada caracter sin saltar y dejando un espacio en blanco entre cada uno



palabra="holan@quetal"
buscar="@" in palabra#Verifica si se encuentra la  @ en buscar 
print("\n") 
if buscar:#Si se encuentra muestra un mensaje 
	print("si se encuentra")
else:
	print("no se encuentra")	

print("\n")

for i in "fabricioGonzalez":
	print("Mi nombre ", end=" ")	


print("\n")
for i in ["hola","Adios","cinco",3]:
	print(str(i) + "  hola")	