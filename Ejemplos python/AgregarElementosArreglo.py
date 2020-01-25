carreras=["Informática","Contabilidad","Lenguas","Derecho","Ingeniería civil","Ingienería en sistemas","Banca y Finanzas"]
print(carreras[:])

#Para añadir elementos a la lista en la última posición(APPEND)
carreras.append("Comercio Internacional")#Agrega los elementos al final de la lista, Solo se puede agregar uno a la vez 
print(carreras[:])

#Para insertar un elemento a la lista en una posición específica(INSERT)
carreras.insert(3,"Español")
print(carreras[:]) 

#Agregar más de un elemento a la lista (EXTEND) se abre parentesís y luego corchetes
refrescos=["Mango"]
print(refrescos[:])
refrescos.extend(["Pera","Uva","Manzana","Sandia"])
print(refrescos[:])

#Saber el índice donde se encuentra un dato
print("El índice de Uva es: ",refrescos.index("Uva"))
refrescos.insert(4,"Melones")
refrescos.extend(["Guayaba","Fresa"])
print(refrescos[:])
print("El índice de sandia es ",refrescos.index("Sandia"))
