import time as t
import utilidades as u
import colores as co
import rondas as ro 

def menu():
    """Menú inicial del juego, en este se verá una pequeña interfaz con el titulo del juego
       y la opción "1) Iniciar" para dar comienzo al juego o la opción "2) Salir" para salir del juego.
    """
    while True:
        u.lista_personas.clear
        print ('\033[2J')   
        print (chr(27) + "[2J")
        print (co.blue)
        print ("!!Patron de Frutas!!")
        print (co.yellow)
        print ("\n")
        print ("1) Iniciar")
        print ("2) Salir")
        print ("\n",co.green)
        opt=int(input ("Digite 1 para iniciar el juego o 2 para salir: "))
        if opt==1:
            print (chr(27) + "[2J")
            print (co.green)
            nombre=input ("ingrese un Jugador: ")
            print ('\033[2J')
            u.insertar(nombre)
            iniciar_juego()      
        elif opt==2:
            exit()
      
        print (chr(27) + "[2J")

def iniciar_juego():
    """Submenú del juego en el cual se agregará el primer jugador. En este menú se presentan
       varias opciones, como la de agregar más jugadores a la partida, ir al apartado de reglas
       en el cual se explica un poco como se juega y la opción de iniciar la partida.
       Además, en la parte superior de este menú se mostrará los jugadores agregados.
    """
    print (chr(27) + "[2J")
    print (co.blue)
    print ("Jugadores:", u.lista_personas)
    print (co.yellow)
    print ("\n")
    print ("1) Agregar otro Jugador")
    print ("2) Jugar")
    print ("3) Reglas")
    print ("\n",co.blue)
    opt=int(input ("Digite alguna de las opciones anteriores: "))
    if opt==1:
        print (chr(27) + "[2J")
        print (co.green)
        nombre=input ("ingrese un Jugador: ")
        print ('\033[2J')
        u.insertar(nombre)
        iniciar_juego()        
    elif opt==2:
        ro.juego()
    elif opt==3:
        reglas()
    else:
        iniciar_juego()
    

def reglas():
    """Apartado de reglas, creado con la funcionalidad de explicar en que consiste el juego
       y como se juega. 
    """
    print (chr(27) + "[2J")
    print (co.yellow)
    print ("Reglas:")
    print ( "El juego consiste en memorizar un patrón de frutas y posteriormente ""\n"
            "ordenar dicho patrón mostrándolo a la pantalla del dispositivo.""\n"
            "  Puede ser jugado por un solo jugador o por una cantidad no definida""\n"
            "de jugadores. El juego será una competencia entre los jugadores por ""\n"
            "ver quien consigue el mínimo de tiempo a la hora de ordenar el patrón,""\n"
            "o bien, si juegas solo puedes tratar de vencer tu propio record.""\n"
            "  El juego consta con 3 niveles de dificultad, cada uno con 5 turnos en""\n"
            "los que los jugadores deberán ordenar un patrón distinto cada turno. ""\n"
            "En cada nivel se aumentará la dificultad añadiendo una mayor cantidad""\n"
            "de frutas al patrón que hay que memorizar.""\n"
            "\n"
            "Nivel 1: Patrón de 3 frutas, 5 turnos.""\n"
            "\n"
            "Nivel 2: Patrón de 4 frutas, 5 turnos.""\n"
            "\n"
            "Nivel 3: Patrón de 5 frutas, 5 turnos.""\n"
            "\n"
            "  Al finalizar los 3 niveles se mostrará una tabla de resultados la cual""\n"
            "mostrará al ganador y al resto de jugadores en base al menor tiempo obtenido""\n"
            "en los 3 niveles.")
    print ("\n",co.red)
    print ("1) volver")
    print ("\n",co.green)
    opt=int(input ("Digite 1 para volver al menú de inicio: "))
    if opt==1:
        iniciar_juego()
    else:
        pass
