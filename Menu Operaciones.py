#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 29 20:21:48 2021
@author: imac
Maria Fernanda Barroso Monroy 
INCO
Ing. Conrado Cruz
Codigo: 218128918
Menu
"""
num1=int(input("Ingrese el primer numero:"))
num2=int(input("Ingrese el segundo numero:"))
while True:
    print(f"Operación a realizar: {num1} y {num2}\n\
Presiona m para multiplicar.\n\
Presiona d para dividir.\n\
Presiona s para sumar.\n\
Presiona r para restar.\n\
Presiona x para salir.")
    opcion=input()
    if opcion=='m':
        print(f"Este es el resultado de la multiplicacion {num1*num2}")
    elif opcion=='d':
        print(f"Este es el resultado de la divicion {num1/num2}")
    elif opcion=='s':
        print(f"Este es el resultado de la suma {num1+num2}")
    elif opcion=='r':
        print(f"Este es el resultado de la resta {num1-num2}")
    elif opcion=='x':
        break
    
