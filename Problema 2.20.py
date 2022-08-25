#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 00:37:15 2021

@author: imac
"""

#Problema 2.20
#Alumna: Maria Fernanda Barroso Monroy 
#Maestro: Ingeniero Conrado Cruz
#Codigo: 218128918
# Fundamentos Filosoficos de la Computacion 

print("Su calificacion de examen parte de 10 a 100.")

exam1 = int(input("Ingrese la calificacion del 1er examen:"))
exam2 = int(input("Ingrese la calificacion del 2do examen:"))
exam3 = int(input("Ingrese la calificacion del 3er examen:"))



prom = exam1 / 100 * 25 
prom1 = exam2 / 100 * 25 
prom2 = exam3 / 100 * 50

suma = prom + prom1 + prom2

print("Su promedio final es:",suma)

