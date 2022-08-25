#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 13:00:37 2021

@author: imac
"""


"""
Maria Fernanda Barroso Monroy
Maestro. Ing. Conrado Cruz
Problema 3.6
"""
"""
Determine el costo y el descuento que tendrá 
un articulo. Considere que si su precio es mayor
 o igual a $200 se le aplica  descuento de 15%,
 y si su precio es mayor a $100 pero menor
 que $200, el descuento es de 12%, y si es menor
 a $100, solo 10%. 
"""

producto=des1=suma1=descuento1=descuento2=des2=suma2=descuento3=des3=suma3=int()

producto=float(input("Ingrese el costo del producto:"))

if producto>200:
    des1= 15/100*producto 
    suma1=producto-des1
    
else:
    if producto>100<200:
        des2=12/100*producto
        suma2=des2-producto
        
if producto<100:
    des3=10/100*producto
    suma3=des3-producto
    
print("El precio final con el descuento es:",suma1)
print("El precio final con el descuento es:",suma2)
print("El precio final con el descuento es:",suma3)      
    



