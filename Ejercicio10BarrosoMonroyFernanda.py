"""
Fundamentos Filosoficos de la computción 
Maria Fernanda Barroso Monroy 
Ing. Conrado Cruz
Fecha: 18/05/2021
Un teatro otorga descuentos según la edad del cliente, guardar las 
edades en un vector de N elementos, determinar la
cantidad de dinero que el teatro deja de percibir por cada una de las categorías. 
Tomar en cuenta que los niños menores de5 años no pueden entrar al 
teatro y que existe un precio único en los asientos.
"""
import os
#Declaracion de variables

Edad=N=c=int()
CantNoPerc1=CantNoPerc2=CantNoPerc3=CantNoPerc4=CantNoPerc5=float()
Precio=30
Cont1=Cont2=Cont3=Cont4=Cont5=int(0)
P1=0.35;P2=0.25;P3=0.10
#Leer el total de boletos vendidos
N=int(input('Cuantos boletos fueron vendidos --->'))
#Ciclo for para lectura de edades
for c in range(N):
    Edad=int(input(f'Dame la edad para el boleto {c+1}-->'))
    #Evaluar la edad
    if Edad >= 5 and Edad <=14:
        Cont1+=1
        print('\nTiene un descuento del 35%..\n')
    else:
        if Edad >=15 and Edad <=19:
            Cont2+=1
            print('\n Tiene un descuento del 25%..\n')
        else:
            if Edad >=20 and Edad <=45:
                Cont3+=1
                print('\nTiene un descuento del 10%..\n')
            else:
                if Edad >=46 and Edad <=65:
                    Cont4+=1
                    print('\nTiene un descuento del 25%..\n')
                else:
                    if Edad >= 66:
                        Cont5+=1
                        print('\nTiene un descuento del 35%..\n')
                    else:
                        print('\nNO PUEDE ENTRAR AL TEATRO POR SER MENOR DE 5 AÑOS..\n')
#Calculos
CantNoPerc1=Precio*Cont1*P1
CantNoPerc2=Precio*Cont2*P2
CantNoPerc3=Precio*Cont3*P3
CantNoPerc4=Precio*Cont4*P2
CantNoPerc5=Precio*Cont5*P1
#Mostrar resultados descuentos por categorias
print('\n\t\tTOTAL DE DESCUENTOS POR CATEGORIAS')

print(f'\nTotal sin percibir categoría 1 35% menos -->${CantNoPerc1} pesos\n')
print(f'\nTotal sin percibir categoría 2 25% menos -->${CantNoPerc2} pesos\n')
print(f'\nTotal sin percibir categoría 3 10% menos -->${CantNoPerc3} pesos\n')
print(f'\nTotal sin percibir categoría 4 25% menos -->${CantNoPerc4} pesos\n')
print(f'\nTotal sin percibir categoría 5 35% menos -->${CantNoPerc5} pesos\n')
print("Gracias por su compra")

os.system('Pause')
#Fin del proceso