"""
Fundamentos Filosoficos de la computción 
Maria Fernanda Barroso Monroy 
Ing. Conrado Cruz
Fecha: 18/05/2021
Una persona debe realizar un muestreo con 50 personas, guardar las edades de las 50 personas y para determinar el
promedio de peso de los niños, jóvenes, adultos y viejos que existen en su zona habitacional (cada una de las categorías se
pudieran guardar las edades en un vector).
"""
#Declaracion de Variables

nino = 0
jovenes = 0
adultos = 0
viejos = 0
peson=0
pesoj=0
pesoa=0
pesov=0
pron=0
proj=0
proa=0
prov=0
x=1
#Procesos
for x in range(1,11):
    print("persona ",x)
    edad=float(input("ingresa tu edad "))
    peso=float(input("ingresa tu peso "))
    if edad<0:
                    print("ingrese una edad correcta")
    if edad>=0 and edad<=12:
                    peson=peson+peso
                    nino=nino+1
                    pron=peson/nino
    if edad>=13 and edad<=29:
                    pesoj=pesoj+peso
                    jovenes=jovenes+1
                    proj=pesoj/jovenes
    if edad>=30 and edad<=59:
                    pesoa=pesoa+peso
                    adultos=adultos+1
                    proa=pesoa/adultos
    if edad>60:
                                    pesov=pesov+peso
                                    viejos=viejos+1
                                    prov=pesov/viejos
#Mostrar resultados
print("El promedio de peso de los niños es de: ",pron)
print("El promedio de peso de los jovenes es de: ",proj)
print("El promedio de peso de los adultos es de: ",proa)
print("El promedio de peso de los viejos es de: ",prov)
#Fin del proceso