#Crear un diccionario con los paises y los mejores equipos de los paises 
equipos={"España":["Barcelona","Real Madrid","Atletico de Madrid","Valencia"],"Italia":["Juventus","Roma","Milan","Inter"]}
print(equipos)
print("Las llaves del diccionario son:",equipos.keys())#Imprime las llaves del diccionario 
print("Los valores de las llaves son ",equipos.values())
print("La cantidad de llaves en el diccionario son:",len(equipos))

#Agregar una nueva clave con valores al diccionario 
equipos["Inglaterra"]=["Arsenal","Manchester United","Manchester City","Chelsea","Liverpool"]
print(equipos)

#Verificar si existe la clave Inglaterra 
if ("Inglaterra" in equipos)==True:
	print("La clave inglaterra si existe y sus valores son :  ")
	print(equipos["Inglaterra"])
else:
	print("No existe la clave")	

#un diciionario dentro de otro	
equipos={"España":{"Equipo":["Barcelona","Real Madrid","Atletico de Madrid","Valencia"]},"Italia":["Juventus","Roma","Milan","Inter"]}
print(equipos.keys())
print(equipos["España"])
