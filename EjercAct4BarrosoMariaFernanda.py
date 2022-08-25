#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 11:17:42 2021

@author: imac
"""

mOe=int(input(chr(27)+"[1;35m""+""Medallas de oro obtenidas por EU:"))
mPe=int(input(chr(27)+"[1;35m""+""Medallas de plata obtenidas por EU:"))
mBe=int(input(chr(27)+"[1;35m""+""Medallas de bronce obtenidas por EU:"))
mOa=int(input(chr(27)+"[1;35m""+""Medallas de oro obtenidas por Alemania:"))
mPa=int(input(chr(27)+"[1;35m""+""Medallas de plata obtenidas por Alemania:"))
mBa=int(input(chr(27)+"[1;35m""+""Medallas de broce obtenidas por Alemania:"))
mOc=int(input(chr(27)+"[1;35m""+""Medallas de oro obtenidas por Cuba:"))
mPc=int(input(chr(27)+"[1;35m""+""Medallas de plata obtenidas por Cuba:"))
mBc=int(input(chr(27)+"[1;35m""+""Medallas de bronce obtenidas por Cuba:"))
mOm=int(input(chr(27)+"[1;35m""+""Medallas de oro obtenidas por Mexico:"))
mPm=int(input(chr(27)+"[1;35m""+""Medallas de plata obtenidas por Mexico:"))
mBm=int(input(chr(27)+"[1;35m""+""Medallas de bronce obtenidas por Mexico:"))

Pais1="EU"
Pais2="Alemania"
Pais3="Cuba"
Pais4="Mexico"

totalm=mOe+mPe+mBe+mOa+mPa+mBa+mOc+mPc+mBc+mOm+mPm+mBm
promediofinal=mOe+mPe+mBe+mOa+mPa+mBa+mOc+mPc+mBc+mOm+mPm+mBm/12
p1=mOe+mPe+mBe
p2=mOe+mPe+mBe
p3=mOc+mPc+mBc
p4=mOm+mPm+mBm
prom1=p1/3
prom2=p2/3
prom3=p3/3
prom4=p4/3
puntaje1=(mOe*50)+(mPe*30)+(mBe*25)
puntaje2=(mOa*50)+(mPa*30)+(mBa*25)
puntaje3=(mOc*50)+(mPc*30)+(mBc*25)
puntaje4=(mOm*50)+(mPm*30)+(mBm*25)

if p1==Pais1:
    prom1=p1/3
else:
    if p1==Pais1:
        puntaje1=(mOe*50)+(mPe*30)+(mBe*25)
    else:
        if p2==Pais2:
            prom2=p2/3
        else:
                if p2==Pais2:
                    puntaje2=(mOa*50)+(mPa*30)+(mBa*25)
                else:
                        if p3==Pais3:
                           prom2=p2/3
                        else:
                            if p3==Pais3:
                                puntaje3=puntaje1=(mOc*50)+(mPc*30)+(mBc*25)
                            else:
                                if p4==Pais4:
                                    prom4=p4/3
                                else:
                                    if p4==Pais4:
                                        puntaje4=(mOm*50)+(mPm*30)+(mBm*25)
                                    else:
                                        
                                        
                                        print("¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬")
                                        print(chr(27)+"[1;35m""+"+"Lugar\tPais\t\tOro\tPlata\tBronce")
                                        print("¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬")
                                        print(chr(27)+"[1;35m""+"+f'1\t{Pais1}\t\t\t{mOe}\t\t{mPe}\t\t{mBe}\n')
                                        print("¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬")
                                        print(chr(27)+"[1;35m""+"+f' 2\t{Pais2}\t\t{mOa}\t\t{mPa}\t\t{mBa}\n')
                                        print("¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬")
# =============================================================================
#                                         print(chr(27)+"[1;35m""+"+f' 3\t{Pais3}\t\t\t{mOc}\t\t{mPc}\t\t{mBc}\n')
# =============================================================================
                                        print("¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬")
                                        print(chr(27)+"[1;35m""+"+f' 4\t{Pais4}\t\t{mOm}\t\t{mPm}\t\t{mBm}\n')
                                        print("¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬")
                                        print(chr(27)+"[1;35m""+"+"Medallas EU:",p1)
                                        print(chr(27)+"[1;35m""+"+"Medallas Alemania:",p2)
                                        print(chr(27)+"[1;35m""+"+"Medallas Cuba:",p3)
                                        print(chr(27)+"[1;35m""+"+"Medallas Mexico:",p4)
                                        print(chr(27)+"[1;35m""+"+"Promedio EU:",prom1)
                                        print(chr(27)+"[1;35m""+"+"Promedio Alemania:",prom2)
                                        print(chr(27)+"[1;35m""+"+"Promedio Cuba:",prom3)
                                        print(chr(27)+"[1;35m""+"+"Promedio Mexico:",prom4)
                                        print(chr(27)+"[1;35m""+"+"Puntaje EU:",puntaje1)
                                        print(chr(27)+"[1;35m""+"+"Puntaje Alemania:",puntaje2)
                                        print(chr(27)+"[1;35m""+"+"Puntaje Cuba:",puntaje3)
                                        print(chr(27)+"[1;35m""+"+"Puntaje Mexico:",puntaje4)
                                        print(chr(27)+"[1;35m""+"+"Total de medallas entregadas:",totalm)
                                        print(chr(27)+"[1;35m""+"+"Promedio de medallas entregadas:",promediofinal)
                                        
                                        
                                        
                                        
                                            
                                        
                                    
                            
                                    
                                
                    
            
            
    



