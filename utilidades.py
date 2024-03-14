"""Archivo de utilidades donde se guardan algunas funciones, listas y diccionarios que serán
utilizados en el código para tenerlos en un lugar organizado.
"""

jugadores_turno={}
jugadores_nivel1={}
jugadores_nivel2={}
jugadores_nivel3={}
lista_personas=[]

def imprimir_frutas(l:list):
    """Esta función recibe una lista con números y los remplaza por nombres de frutas en una
    variable tipo str, para luego imprimir esta variable.

    Args:
        l (list): Lista con un patrón aleatorio de números.
    """
    nombre_frutas=["piña","cereza","uva","pera","guanabana"]
    orden_frutas=""
    for e in l:
                orden_frutas+=nombre_frutas[e]+" "
    print(orden_frutas)

def insertar (nombre:str)->None:
    """Función que se encarga de almacenar el nombre de los jugadores en una lista

    Args:
        nombre (str): nombre de cada jugador que sea añadido
    """
    lista_personas.append((nombre))
