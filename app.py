import ARMem as ar
import time
import agenda as ag

lista_juego=[[0],[1],[0],[0],[0]]

print('\033[2J')  # Código ANSI para limpiar la pantalla en sistemas Windows
tiempo_total=0
cont=0
jugadores=1
for x in lista_juego:
    while jugadores<= len(ag.lista_personas):
        print(f"turno de:", ag.lista_personas[cont] )
        time.sleep(1)
        print(f'Memorice la siguiente secuencia...')
        print(x)
        time.sleep(1)
        print('\033[2J')
        print(f'Ordene los marcadores en el orden que se le indicó!')
        time.sleep(1)
        print('\033[2J')  # Código ANSI para limpiar la pantalla en sistemas Windows
        tiempo_partida=round(ar.start_sorting(x,flip_image=True,show_images=True, show_coordinates=False, show_ids=False, show_identified_marker=False)  ,2)
        tiempo_total+=tiempo_partida
        print(f'Tiempo de partida: {tiempo_partida}s')
        time.sleep(1)
        print('\033[2J')  # Código ANSI para limpiar la pantalla en sistemas Windows
        ag.jugadores_tiempo[ag.lista_personas[cont]]= tiempo_partida
        jugadores+= 1
        cont+= 1
    else:
        for J,T in ag.jugadores_tiempo.items():
            print (f"El jugador", J,"ha completado el turno en un tiempo de", T, "s")