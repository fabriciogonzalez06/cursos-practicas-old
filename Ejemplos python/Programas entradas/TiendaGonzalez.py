#Función para mostrar el menú que va a comprar 
def menuPlatos():
	print("***************************************************************************************************")
	print("*|                             >>>>>>>>TIPICOS OJOJONA<<<<<<<                                     |*")
	print("*|                                                                                                |*")
	print("*|                                         >>MENÚ<<                                               |*")
	print("*|                                                                                                |*")
	print("*|               1)Plato carne de cerdo-------------------------250 Lps                           |*")
	print("*|               2)Plato Carne de Res---------------------------200 Lps                           |*")
	print("*|               3)Plato Pollo Frito----------------------------130 Lps                           |*")	
	print("*|                                                                                                |*")
	print("*|                                                                                                |*")
	print("***************************************************************************************************")

#Función para los refrescos 
def menuRefrescos():
	print("***************************************************************************************************")
	print("*|                                                                                                |*")
	print("*|                                                                                                |*")
	print("*|                                          >>REFRESCOS<<                                         |*")
	print("*|                                                                                                |*")
	print("*|               1)Natural de piña-------------------------25 Lps                                 |*")
	print("*|               2)Natural de Nance------------------------20 Lps                                 |*")
	print("*|               3)Refrsco---------------------------------30 Lps                                 |*")	
	print("*|                                                                                                |*")
	print("*|                                                                                                |*")
	print("***************************************************************************************************")

#Función para calcular subtotal 
def subtotalPlato(precio,cantidad):
	subt=precio*cantidad
	return subt

#Funcion para calcular subtotal refrescos 
def subtotalRefrescos(precio,cantidad):
    subt=precio*cantidad
    return subt

#Función para calcular el descuento en platos de comida 
def descuentoPlatos(subtotalP,descuento):
	des=subtotalP*descuento
	return des

#Función para calcular el descuento en refrescos 
def descuetoRefrescos(subtotalR,descuento):	
	des=subtotalR*descuento
	return des

#Programa principal 
#Invocar metodo menu
menuPlatos()
print("Ingrese el nombre del cliente ")
nombre=input()
print("Ingrese la opción a comprar ")
opcPlato=int(input())
if(opcPlato==1):
	tipoPlato="Plato carne de cerdo"
	precioPlato=250
	print("Ingrese la cantidad de ",tipoPlato,"A llevar")
	cantPlato=int(input())
	#Calcular subtotal Platos
	stPlato=subtotalPlato(precioPlato,cantPlato)#Invocación del metodo 
	#Invocar al metodo de los refrescos 
	menuRefrescos()
	print("Eliga una opcion de refresco")
	opcRefresco=int(input())
	
if(opcRefresco==1):
		tipoRefresco="Refresco natural de piña"
		precioRefresco=25
		print("Ingrese la cantidad de ",tipoRefresco,"A llevar ")
		cantRefresco=int(input())
		#Calcular subtotal en refrescos 
		stRefescos=subtotalRefrescos(precioRefresco,cantRefresco)
	
	
if (opcRefresco==2):

		tipoRefresco="Refresco natural de Nance"
		precioRefresco=20
		print("Ingrese la cantidad de ",tipoRefresco,"A llevar ")
		cantRefresco=int(input())
		#Calcular subtotal en refrescos 
		stRefescos= subtotalRefrescos(precioRefresco,cantRefresco)
		
	
if(opcRefresco==3):
		tipoRefresco="Refresco "
		precioRefresco=30
		print("Ingrese la cantidad de ",tipoRefresco,"A llevar ")
		cantRefresco=int(input())
		#Calcular subtotal en refrescos 
		stRefrescos=subtotalRefrescos(precioRefresco,cantRefresco)
	
if(opcRefresco>3):
		print("Error opción de refresco no válida ")
		tipoRefresco="Sin Refresco"
		cantRefresco=0
		stRefrescos=subtotalRefrescos(0,0)   
		#Calcular descuento según la cantidad de platos de comida a llevar
	
if(cantPlato>=10):
		porcentajeDes=0.15
		desPlatos=descuentoPlatos(stPlato,porcentajeDes)
else:
		porcentajeDes=0.05
		desPlatos=descuentoPlatos(stPlato,porcentajeDes)
    


if(cantRefresco>=15):
		porcentajeDesRefre=0.10
		desR=descuetoRefrescos(stRefrescos,porcentajeDesRefre)
else:

		porcentajeDesRefre=0.05
		desR=descuetoRefrescos(stRefrescos,porcentajeDesRefre)
	#cantidadalcular los subtotales y el isv 
 	isvPlatos=stPlato*0.15
 	isvRefrescos=stRefrescos * 0.15
  	isv=stPlato + stRefrescos
 	descuentoTotal=desPlatos + desR
  	#Calcular total a pagar 
 	totalPagar=stRefrescos + stPlato + isv - descuentoTotal

    print("****************************************Factura****************************************************")
    print("El nombre del cliente es ",nombre)
    print("El tipo de plato a comprar por ",nombre,"es",tipoPlato)
    print("La cantidad a llevar por ",tipoPlato,"es ",cantPlato,"------",precioPlato,"Lps")
    print("El tipo de refresco a comprar es ",tipoRefresco,"Cantidad",cantRefresco,"------",precioRefresco,"Lps")
    print("El subtotal en  ",tipoPlato,"es",stPlato)
    print("El subtotal en ",tipoRefresco,"es",stRefrescos)
    print("El isv en ",tipoPlato,"es ",isvPlatos)
    print("El isv en ",tipoRefresco,"es ",isvRefrescos)
    print("El isv total es ",isv)
    print("El descuento en ",tipoPlato,"es ",desPlatos)
    print("El descuento en ",tipoRefresco,"es ",desR)
    print("El total de descuento es ",descuentoTotal)
    print("El total a pagar es ",totalPagar)
    print("****************************************************************************************************")










