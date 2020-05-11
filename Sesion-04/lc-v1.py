
import os 
import time 

# variables 
                # ""\Users\Desarrollador1\CursoPython\sesion-03>
carpeta = "."   # esto es lo que hace referencia a la carpeta actual

def obtener_elementos(carpeta):
    """
    Obtiene los lementos de la carpeta y regresa en forma de lista 
    """
    
    # obtener la lista de elementos de una carpeta 
    
    nombres = os.listdir ( carpeta) # ["2nom1", "nom2", ...]
    
    # Agregando carpeta a la lista de nombres
    for i, nom in enumerate (nombres): 
        #[0(," nom1)")]
        nombres[i] = os.path.join(carpeta, nom) 
           

    """        esto es  comentarios de recordarorios 
    estructura de datos para incluir el tamaño 
    [
        ["nom1", 1234], 
        ["nom2", 5678],
        ...
    ]
    """
    elementos = []
    total = 0 
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
    
        # sumar el tam a total para cada elemento"
        
        # total = total + tam 
        total += tam
        
        if os.path.isdir(nom):   # si nom es una carpeta ?
            # sub_elementos = obtener_elementos (nom) 
            # lista de elementos - lista de lista 
            sub_elementos, sub_total = obtener_elementos (nom)
            elementos += sub_elementos
            
        
        
    return elementos, total

def imprimir_elementos(elementos, total):
    """"
    imprime la lista de elementos en formato en formato de texto de salida 
    
    """
    # solo falta imprimir- se ingrsa para mostrar en forma de lista 
    for e in elementos:    
        # e = ["nom, 1234,"]
                    #print ("{} {}".format(e [0,e [0]))
        if os.path.isdir(e[0]):
            e[0] +=  "/"
            #  e[0]  =e [0]+"/" 

        print ("{:60} {:10} {:15}".format(*e))
        # va a agregar todos los elementos de e ( e = al nom , 1234, ... )
    #imprimir total 
    print("-" * 40)
    print ("Total: {} Bytes".format(total)) 
        
def main ():
    """es la función principal del script o módulo """
    # llamando a las funciones 
    elementos, total = obtener_elementos (carpeta)
    imprimir_elementos(elementos, total)

# Para poder ejecutarlo como módulo
if __name__ == "__main__":
    main()
