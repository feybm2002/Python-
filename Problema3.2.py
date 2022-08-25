#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 21:02:01 2021

@author: imac
"""

"""
Maria Fernanda Barroso Monroy
Maestro. Ing. Conrado Cruz
Problema 3.2
"""
"""
Realice un algoritmo para determinar el suelo
 semanal de un trabajador con base en las horas
 trabajadas y el pago por hora, considerando que
 después de las 40 horas cada hora se considera 
 como excedente y se paga el doble. 
"""

horas=horas_extra=pago_hora=sueldo1=sueldo2=pro1=pro2=sueldo_final=int()

horas=float(input("Ingrese las horas trabajadas:"))
pago_hora=float(input("Ingrese el sueldo por hora:"))

if horas<=40 :
    sueldo1=pago_hora*horas 
else:
    if horas>40 :
        sueldo2=horas-40
        pro1=sueldo2*pago_hora*2 
        pro2=40*pago_hora
        sueldo_final=pro1+pro2
        
print("Su sueldo con horario normal es de:",sueldo1)
print("Su sueldo con horas extra es de:",sueldo_final)
