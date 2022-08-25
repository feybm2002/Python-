#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 19:26:34 2021

@author: imac
"""

def Inicio():
    ventana['bg'] = 'pink'
   
def Inventario():
    ventana['bg'] = 'blue'

def Ventas():
    ventana['bg'] = 'purple'
    
def Facturas():
    ventana['bg'] = 'pink'
    
def Intro():
    print("Este programa tiene como finalidad volver mas sencillo el trabajo a la hora de hacer ventas, facturas e inventarios.")

def Inicior():
        

import tkinter as tk 
ventana =tk.Tk()
ventana.title("Menu de una tienda (Inventario)")
ventana.geometry("700x400")

mi_menu = tk.Menu(ventana)
mi_menu.add_command(label='Inicio',command=Inicio)
mi_menu.add_command(label='Inventario', command=Inventario)
mi_menu.add_command(label='Ventas', command=Ventas)
mi_menu.add_command(label='Facturas' , command=Facturas)

ventana.config(menu=mi_menu)

ventana.mainloop()

