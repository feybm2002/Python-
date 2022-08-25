"""
Fundamentos Filosoficos de la computción 
Maria Fernanda Barroso Monroy 
Ing. Conrado Cruz
Fecha: 18/05/2021
Suponga que se tiene un conjunto de calificaciones de un grupo de 40 alumnos, 
guardar las calificaciones en un vector. Realizar un algoritmo para calcular 
la calificación media y buscar la calificación más baja y alta de todo el grupo.

"""
#Declaracion de Variables

sc=[10, 4, 9, 2, 6, 5, 9, 10, 5, 7]
#Operaciones
suma_calif=sum(sc)
print(sc)
#Mostrar resultados
print("El valor máximo es:", max(sc))
print("El valor minimo es:", min(sc))
print("El promedio de las calificaciones es de: ",suma_calif/10)
#Fin del proceso
