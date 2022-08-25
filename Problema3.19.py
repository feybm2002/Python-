#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 09:53:12 2021

@author: imac
"""
"""
Maria Fernanda Barroso Monroy
Maestro. Ing. Conrado Cruz
Problema 3.19
"""
"""
La secretaria de salud requiere un diagrama de 
flujo que le represente el algoritmo que permita
 determinar qué tipo de vacuna (A, B o C) debe
 aplicar a una persona, considerando que si es 
 mayor de 70 años, sin importar el sexo, se le 
 aplica la tipo C; si tiene entre 16 y 69 años,
 y es mujer, se le aplica la B, y si es hombre,
 la A; si es menor de 16 años, se le aplica la 
 tipo A, sin importar el sexo. 

""" 
edad=sexo=int()
p=str()

edad=float(input("Ingrese su edad:"))
sexo=float(input("Dame tu sexo, donde 1 es mujer y 2 es hombre:"))

if edad>16<69 and sexo==1:
    p=("B")
    
else:
    if edad>16<69 and sexo==2:
        p=("A")
if edad>70:
    p=("C")
else:
    if edad<16:
        p=("A")
        
print("Su vacuna correspondiente es:",p)
input("Presiona enter para continuar..")


    
    