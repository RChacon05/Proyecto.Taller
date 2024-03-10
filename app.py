import ARMem as ar
import time as t
import colores as co
import utilidades as u

lista_juego=[[0,],[1],[2],[3],[4]]

print('\033[2J')  # Código ANSI para limpiar la pantalla en sistemas Windows
tiempo_total=0
for x in lista_juego:
    turno_jugador = 1
    cont=0
    while turno_jugador<= len(u.lista_personas):
        print('\033[2J')
        print(f"turno de:", u.lista_personas[cont])
        t.sleep(3.5)
        print(f'Memorice la siguiente secuencia...')
        print(co.green)
        u.imprimir_frutas(x)
        t.sleep(5)
        print('\033[2J')
        print(f'Ordene los marcadores en el orden que se le indicó!')
        t.sleep(2.5)
        print('\033[2J')  
        tiempo_partida=round(ar.start_sorting(x,flip_image=True,show_images=True, show_coordinates=False, show_ids=False, show_identified_marker=False)  ,2)
        tiempo_total+=tiempo_partida
        print(f'Tiempo de partida: {tiempo_partida}s')
        t.sleep(3)
        print('\033[2J')  
        u.jugadores_tiempo[u.lista_personas[cont]]= tiempo_partida
        turno_jugador+= 1
        cont+= 1
    else:
        for J,T in u.jugadores_tiempo.items():
            print ("El jugador", J,"ha completado el turno en un tiempo de", T, "s")
            t.sleep(1)