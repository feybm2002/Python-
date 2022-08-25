

"""
Maria Fernanda Barroso Monroy 
Codigo: 218128918
INCO
Ing. Conrado Cruz
Problema 3 
"""
nombre=correo=str()
cantidad=tipo=int()

nombre=str(input("Ingrese su nombre:"))
correo=str(input("Ingrese su correo:"))
tipo=float(input("Tipo de silla que desea:, ponga 0 si es A, 1 si es B, 2 si es C."))
cantidad=float(input("Ingrese la cantidad de sillas:"))

if tipo==0:
    A=cantidad<6
    totalA=cantidad*8
    print("Precio final:",totalA)
else:
        if tipo==0:
            A=cantidad>6
            totalA=3*8/100*cantidad
            print("Precio final:",totalA)
        else:
                
            if tipo==1:
                B=cantidad<6 
                totalB=cantidad*10
                print("Precio final:",totalB)
            else:
                    if tipo==1:
                        B=cantidad>6
                        totalB=5*10/100*cantidad 
                        print("Precio final:",totalB)
                    else:
                            if tipo==2:
                                C=cantidad<6
                                totalC=cantidad*15 
                                print("Precio final:",totalC)
                            else:
                                    if tipo==2:
                                        C=cantidad>6
                                        totalC=7/15*100*cantidad
                                        print("Precio final:",totalC)
                                
                                        
print("Factura tiendita las sillas, Cliente:",nombre,correo)
                                         
                               

                                         
                                         
                                    
                                         
                                         
                                        
                                
    
    
