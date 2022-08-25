#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 17:46:14 2021

@author: imac
"""

#Fundamentos filosoficos de la computacion
#Maestro: Ing. Conrado Cruz
#Alumna: Maria Fernanda Barroso Monroy
#INCO 
#Problema 8

tiempo = int(input("Ingrese tiempo en segundos:"))
angulo = int(input("Ingrese angulo:"))

velocidad = tiempo * 9.81 / angulo 

print("La velocidad inicial es:",velocidad)
