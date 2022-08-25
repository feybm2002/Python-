#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 08:30:17 2021

@author: imac
"""

personas=platillo=int()

personas=float(input("Ingrese el numero de personas para el banquete:"))

if personas<200:
    platillo= 95
    
else:
    if personas>200<300:
        platillo= 85
        
if personas>300:
    platillo= 75 
    
print("El precio final por platillo sera de:",platillo)

