#programa que cuenta los números pares hasta 100

i=1
contPares=0

while i<=100:
	if i % 2==0:
		contPares=contPares+1
		print(i,end=" ")
	i=i+1	

print("\n\n La cantidad de pares es " + str(contPares))	