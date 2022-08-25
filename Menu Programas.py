#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 29 20:45:41 2021
@author: imac

Maria Fernanda Barroso Monroy 
INCO
Ing. Conrado Cruz
Codigo: 218128918
Menu
"""
prog=int(input("Ingrese el programa que desea usar:"))
while True:
    print(f"Operación a realizar: {prog}\n\
Presiona 1 para sacar promedio.\n\
Presiona 2 para sacar calificacion.\n\
Presiona 3 para sacar datos.\n\
Presiona 4 para sacar descuentos.\n\
Presiona 5 para sacar edades.\n\
Presiona 6 para salir.")
    opcion=float()
    

if opcion=='1':
print("
grupo=0
mujer=0
hombre=0
edadh=0
edadm=0
edadg=0
proh=0
prom=0
prog=0

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
                            
                                print("El promedio de edad de los hombres es de: ",proh)
                                print("El promedio de edad de las mujeres es de: ",prom)
                                print("El promedio de edad del grupo es de: ",prog)
               ")  
               elif opcion=='2':
                   print("
                            
def proceso():
    sc=[10, 4, 9, 2, 6, 5, 9, 10, 5, 7]
  
    suma_calif=sum(sc)
    print(sc)
   
    print("El valor máximo es:", max(sc))
    print("El valor minimo es:", min(sc))
    print("El promedio de las calificaciones es de: ",suma_calif/10)
if __name__ == '__main__':  
    proceso()
    ")
    
 elif opcion=='3':
     print("
    
def proceso():
    ama=0
    rosa=0
    roja=0
    verd=0
    azul=0
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

                                    print("El numero de autos con calcomania amarilla es de: ",ama)
                                    print("El numero de autos con calcomania rosa es de: ",rosa)
                                    print("El numero de autos con calcomania roja es de: ",roja)
                                    print("El numero de autos con calcomania verde es de: ",verd)
                                    print("El numero de autos con calcomania azul es de: ",azul)
                               
if __name__ == '__main__':
    proceso()
    ")
    
     elif opcion=='4':
         print("
    
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

print("El promedio de peso de los niños es de: ",pron)
print("El promedio de peso de los jovenes es de: ",proj)
print("El promedio de peso de los adultos es de: ",proa)
print("El promedio de peso de los viejos es de: ",prov)   
    
")

 elif opcion=='5':
     print("

import os

def imprimir():
    print('\n\t\tTOTAL DE DESCUENTOS POR CATEGORIAS')
    print(f'\nTotal sin percibir categoría 1 35% menos -->${CantNoPerc1} pesos\n')
    print(f'\nTotal sin percibir categoría 2 25% menos -->${CantNoPerc2} pesos\n')
    print(f'\nTotal sin percibir categoría 3 10% menos -->${CantNoPerc3} pesos\n')
    print(f'\nTotal sin percibir categoría 4 25% menos -->${CantNoPerc4} pesos\n')
    print(f'\nTotal sin percibir categoría 5 35% menos -->${CantNoPerc5} pesos\n')
    print("Gracias por su compra")
Edad=N=c=int()
CantNoPerc1=CantNoPerc2=CantNoPerc3=CantNoPerc4=CantNoPerc5=float()
Precio=30
Cont1=Cont2=Cont3=Cont4=Cont5=int(0)
P1=0.35;P2=0.25;P3=0.10

N=int(input('Cuantos boletos fueron vendidos --->'))

for c in range(N):
    Edad=int(input(f'Dame la edad para el boleto {c+1}-->'))
    
    if Edad >= 5 and Edad <=14:
        Cont1+=1
        print('\nTiene un descuento del 35%..\n')
    else:
        if Edad >=15 and Edad <=19:
            Cont2+=1
            print('\n Tiene un descuento del 25%..\n')
        else:
            if Edad >=20 and Edad <=45:
                Cont3+=1
                print('\nTiene un descuento del 10%..\n')
            else:
                if Edad >=46 and Edad <=65:
                    Cont4+=1
                    print('\nTiene un descuento del 25%..\n')
                else:
                    if Edad >= 66:
                        Cont5+=1
                        print('\nTiene un descuento del 35%..\n')
                    else:
                        print('\nNO PUEDE ENTRAR AL TEATRO POR SER MENOR DE 5 AÑOS..\n')

CantNoPerc1=Precio*Cont1*P1
CantNoPerc2=Precio*Cont2*P2
CantNoPerc3=Precio*Cont3*P3
CantNoPerc4=Precio*Cont4*P2
CantNoPerc5=Precio*Cont5*P1

if __name__ == '__main__':
    imprimir()
os.system('Pause')
")

  elif opcion=='6':
        break
    


    
    