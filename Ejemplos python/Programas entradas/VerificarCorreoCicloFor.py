#Pedir el correo electrónico 
correo=input("Ingrese su direción de correo >")
print("Longitud de correo " + str(len(correo)))
contadorArroba=0
contadorPunto=0
#Ciclo for para recorrer el ciclo for y verificar si es correcto
for i in correo:
	verificar=True
	if i=="@":
		contadorArroba=contadorArroba+1

	if i==".":
		contadorPunto=contadorPunto+1

	if contadorArroba>1 or contadorPunto==0 or contadorPunto>3:
		verificar=False 	


if verificar:
	print("Su correo es válido")
else:
	print("Su correo es inválido")			

		