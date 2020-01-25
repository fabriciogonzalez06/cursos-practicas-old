#Método para calcular el promedio j
def promedio(prom):
	return prom/4



#definir variables 
nombre=""
notas=0
acumPrimerParcial=0
acumSegundoParcial=0
acumTercerParcial=0
acumCuartoParcial=0
promPrimerP=0
promSegundoP=0
promTercerP=0
promCuarto=0
promedioGoblal=0
contador=0
#Pedir nombre del alumno 
nombre=input("\n Ingrese el nombre del alumno >")
#Implementar ciclo for para calcular nota 
for i in range(16):
	
	if i>=0 and i<=3:#Para notas del primer parcial 
		if i==0:#Si vale uno contador vale cero para empezar a contar desde 1 las notas de todos los parciales 
			contador=0
		
		notas=float(input("Ingrese la nota " + str(contador+1) + " del " + "Primer parcial de " + nombre + " >"))#Se pide la nota si entra en la condición para primer
		acumPrimerParcial=acumPrimerParcial+notas


	if i>=4 and i<=7:
		if i==4:
			contador=0
		
		notas=float(input("Ingrese la nota " + str(contador+1) + " del " + "Segundo  parcial de " + nombre + " >"))
		acumSegundoParcial=acumSegundoParcial+notas	


	if i>=8 and i<=11:
		if i==8:
			contador=0
		
		notas=float(input("Ingrese la nota " + str(contador+1) + " del " + "tercer  parcial de " + nombre + " >"))
		acumTercerParcial=acumTercerParcial+notas

	if i>=12:
		if i==12:
			contador=0
	   
		notas=float(input("Ingrese la nota " + str(contador+1) + " del " + "Cuarto  parcial de " + nombre + " >"))
		acumCuartoParcial=acumCuartoParcial+notas

	#Incrementar contador 
	contador=contador+1


#Calcular promedios Llamando a la función para calcular el promedio de los parciales 
print("\n El promedio del primer parcial de " + nombre + " es " + str(promedio(acumPrimerParcial)))
print("\n El promedio del Segundo parcial de " + nombre+ " es " + str(promedio(acumSegundoParcial)))
print("\n El promedio del Tercer  parcial de " + nombre+" es " + str(promedio(acumTercerParcial)))
print("\n El promedio del Cuarto parcial de " + nombre+ " es " + str(promedio(acumCuartoParcial)))

promedioGoblal=(promedio(acumPrimerParcial) + promedio(acumSegundoParcial) + promedio(acumTercerParcial) + promedio(acumCuartoParcial))/4
print("\n El promedio globlal de " + nombre+ " es " + str(promedioGoblal))

