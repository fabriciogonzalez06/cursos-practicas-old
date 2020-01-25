print("Programa de evaluacion de notas de alumno")

#Función para evaluación de nota 
def evaluacion(nota):
	valoracion="Aprobado"
	if (nota<6):
		valoracion="Reprobado"
	return valoracion	

nota_alumno=int(input("Ingrese la nota del alumno:"))

#Llamar a la función evaluación y mandarle un parámetro de nota
print(evaluacion(7))	