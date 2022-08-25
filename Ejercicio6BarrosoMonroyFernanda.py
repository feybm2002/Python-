"""
Fundamentos Filosoficos de la computción 
Maria Fernanda Barroso Monroy 
Ing. Conrado Cruz
Fecha: 18/05/2021
El Depto. de Seguridad Publica y Transito del D.F. desea saber, de los n autos que entran a la ciudad de México, cuantos
entran con calcomanía de cada color. Conociendo el último dígito de la placa de cada automóvil se puede determinar el
color de la calcomanía
"""
#Declaracion de variables
ama=0
rosa=0
roja=0
verd=0
azul=0
#Procesos
print("Para detener, escribir '-1' en placa")
repetir='b'
while repetir=='b':
                digito=float(input("ingrese el ultimo digito de la placa: "))
                if digito==1 or digito==2:
                                ama=ama+1
                                print("Este auto tiene una calcomania amarilla")
                if digito==3 or digito==4:
                                rosa=rosa+1
                                print("Este auto tiene una calcomania rosa")
                if digito==5 or digito==6:
                                roja=roja+1
                                print("Este auto tiene una calcomania roja")
                if digito==7 or digito==8:
                                verd=verd+1
                                print("Este auto tiene una calcomania verde")
                if digito==9 or digito==0:
                                azul=azul+1
                                print("Este auto tiene una calcomania azul")
                if digito==-1:
                                repetir='c'
                                #Mostrar resultados
                                print("El numero de autos con calcomania amarilla es de: ",ama)
                                print("El numero de autos con calcomania rosa es de: ",rosa)
                                print("El numero de autos con calcomania roja es de: ",roja)
                                print("El numero de autos con calcomania verde es de: ",verd)
                                print("El numero de autos con calcomania azul es de: ",azul)
#Fin del proceso