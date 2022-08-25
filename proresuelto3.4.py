#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 07:20:48 2021

@author: imac
"""

costo=des1=pro1=pro2=descuento=int()


costo=float(input("Ingrese el costo del traje:"))

if costo>2500:
    pro1= 15/100*costo 
    des1= costo-pro1 
    descuento= 15 
    
else:
    if costo<2500:
        pro2= 8/100*costo 
        des1= costo-pro2
        descuento= 8 
        
print("El costo final con su descuento aplicado es:",des1)
print("Su porcentaje de descuento fue del:",descuento)
