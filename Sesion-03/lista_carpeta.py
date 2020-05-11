
import os 
import time 

# variables 
                # ""\Users\Desarrollador1\CursoPython\sesion-03>
carpeta = "."   # esto es lo que hace referencia a la carpeta actual

def obtener_elementos(carpeta):
    """
    Obtiene los lementos de la carpeta y regresa en forma de lista 
    """
    
    # obtener la lista de elemantos de una carpeta 
    nombres = os.listdir ( carpeta) # ["2nom1", "nom2", ...]

    """        esto es  comentarios de recordarorios 
    estructura de datos para incluir el tamaño 
    [
        ["nom1", 1234], 
        ["nom2", 5678],
        ...
    ]
    """
    elementos = []
    for nom in nombres:
        if os.path.isfile(nom):     # si es archivo - : calcula el tamaño  
            tam = os.path.getsize(nom)
        else: # si es una carpeta entonces 
            tam= 0

        # para obtener la fecha 
        fecha = os.path.getmtime(nom)
        fecha = time.ctime(fecha)

        elemento = [nom, tam, fecha]
        elementos.append(elemento)
    return elementos

def imprimir_elementos(elementos):
    """"
    imprime la lista de elementos en formato en formato de texto de salida 
    
    """
    # solo falta imprimir- se ingrsa para mostrar en forma de lista 
    for e in elementos:
                #print ("{} {}".format(e [0,e [1]))
        print ("{:30} {:10} {:15}".format(*e))  # va a agretgar todos los elementos de e ( e = al nom , 1234, ... )


# llamando a las funciones 
elementos = obtener_elementos (carpeta)
imprimir_elementos ( elementos)

