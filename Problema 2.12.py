#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 20:51:13 2021

@author: imac
"""

#Problema 2.12
#Alumna: Maria Fernanda Barroso Monroy 
#Maestro: Ingeniero Conrado Cruz
#Codigo: 218128918
# Fundamentos Filosoficos de la Computacion 

producto = int(input("Ingrese precio del producto:"))

descuento1 = 20 * producto / 100
descuento2 = producto - descuento1 

print("El descuento del produto es:", descuento2)

iva = descuento2 * 15 / 100 
iva2 = iva + descuento2

print("El precio final es:",iva2)
