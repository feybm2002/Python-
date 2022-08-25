"""
Fundamentos Filosoficos de la computción 
Maria Fernanda Barroso Monroy 
Ing. Conrado Cruz
Fecha: 18/05/2021
Calcular el promedio de edades y guardarlas en un vector de hombres y otro de mujeres y de todo un grupo de alumnos.
Al final hay que mostrar cada uno de los tres vectores Hombre, Mujeres y Grupo.
"""

def proceso():
    grupo=0
    mujer=0
    hombre=0
    edadh=0
    edadm=0
    edadg=0
    proh=0
    prom=0
    prog=0
    #Procesos
    print("Para detener, escribir 'para' en pregunta de genero")
    repetir='b'
    while repetir=='b':
                    g=str(input("Escriba si es hombre o mujer: "))
                    edad=float(input("Escriba su edad: "))
                    if g=='hombre':
                                    hombre=hombre+1
                                    grupo=grupo+1
                                    edadh=edadh+edad
                                    edadg=edadg+edad
                                    proh=edadg/hombre
                    if g=='mujer':
                                    mujer=mujer+1
                                    grupo=grupo+1
                                    edadm=edadm+edad
                                    edadg=edadm+edad
                                    prom=edadm/mujer
                    if g=='para':
                                    repetir='c'
                                    prog=(edadm+edadh)/grupo
                                    #Mostrar resultados
                                    print("El promedio de edad de los hombres es de: ",proh)
                                    print("El promedio de edad de las mujeres es de: ",prom)
                                    print("El promedio de edad del grupo es de: ",prog)
#Mostrar resultados
if __name__ == '__main__':
    proceso()
#Fin del proceso