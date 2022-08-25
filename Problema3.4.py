#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 11:32:07 2021

@author: imac
"""

"""
Maria Fernanda Barroso Monroy
Maestro. Ing. Conrado Cruz
Problema 3.4
"""
"""
El dueño de un estacionamiento requiere un diagrama de flujo con el
 algoritmo que le permita determinar cuanto debe cobrar por el uso de 
 estacionamiento a sus clientes. Las tarifas que se tienen 
 son las siguientes:
Las dos primeras horas a $5.00 c/u.
Las siguientes tres a $4.00 c/u.
Las cinco siguientes a $3.00 c/u.
Después de diez horas el costo por cada una es de $2.00.
"""

horas=hora1=hora2=pro0=pro01=hora3=pro1=pro2=hora4=pro3=pro4=total=int()

horas=float(input("Ingrese las horas que estuvo en el estacionamiento:"))

if horas<=2:
    hora1=horas*5 
else:
    if horas<=5:
        pro0=horas-2
        pro01=pro0*4
        hora2=pro01+10
        
if horas<=10:
   pro1=horas-5
   pro2=pro1*3
   hora3=pro2+22
   
else:
    if horas>10:
      pro3=horas-10
      pro4=pro3*2
      hora4=pro4+37
        
print("El costo final es:",hora1)
print("El costo final es:",hora2)
print("El costo final es:",hora3)
print("El costo final es:",hora4)
