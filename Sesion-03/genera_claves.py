import random

n = 5 
m = 10 

                #lista de símbolos 
minusculas = "abcdefghijklmnopqrstuvwxyz"
mayusculas = minusculas.upper()   # camibia a minusculas 
digitos = "1234567890"
simbolo = "*/#-$%&@"
alfabeto = minusculas + mayusculas + digitos + simbolo



for i in range (n):
                    # Crea una sóla clave 
    clave = random.choice(minusculas) #elegir una minuscula al azar. ejemplo clave = "k"
                    # clave = clave + random.choice (mayusculas) #clave = "kR"
    clave += random.choice (mayusculas) #clave = "kR"
    clave += random.choice (digitos) #clave = "kR3"
    clave += random.choice (simbolo) #clave = "kR3"


    r = m - 4 # calculamos cuantas nos faltan  ej 5 
    faltantes = random.choices(alfabeto, k=r) # regresa una "aBr3s" 

    faltantes = "".join (faltantes) # " aBr3s
    clave += faltantes #KraBr3s
    lclave = list (clave)  # esto lo que hace es convertir la clave a una   list para poder mesclarlas por que solo puede hacerse en list
    random.shuffle (lclave) # esto es el que mezcla las letras 
    clave = "".join(lclave) # este lo que hace es juntarlo 
    print (clave)
    
    
