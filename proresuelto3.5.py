#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 08:23:18 2021

@author: imac
"""

cantidad=int()
a=str()

cantidad=float(input("Ingrese una cantidad del 1 al 10,000:"))

if cantidad>1<100 :
    a= "Cantidad menor"
    
else:
    if cantidad>100<1000:
        a= "Cantidad mediana"
        
if cantidad>1000<10000:
    a= "cantidad mayor"
    
print("Su cantidad es una:",a)

