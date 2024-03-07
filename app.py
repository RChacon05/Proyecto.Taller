import ARMem as ar
import time
import agenda as ag
lista_juego=[[0,1,2,3,4],[4,3,2,1,0],[4,3,2,1,0],[0,2,1,4,3],[3,4,2,0,1]]

print('\033[2J')  # Código ANSI para limpiar la pantalla en sistemas Windows
tiempo_total=0
cont=0
for x in lista_juego:
    print(f"turno de:", ag.lista_personas[cont] )
    time.sleep(2)
    print(f'Memorice la siguiente secuencia...')
    print(x)
    time.sleep(5)
    print(f'Ordene los marcadores en el orden que se le indicó!')
    time.sleep(3)
    
    print('\033[2J')  # Código ANSI para limpiar la pantalla en sistemas Windows

    tiempo_partida=round(ar.start_sorting(x,flip_image=True,show_images=True, show_coordinates=False, show_ids=False, show_identified_marker=False)  ,2)
    tiempo_total+=tiempo_partida
    print(f'Tiempo de partida: {tiempo_partida}s')

    time.sleep(3)
    print('\033[2J')  # Código ANSI para limpiar la pantalla en sistemas Windows
 
    ag.lista_personas[cont]= ag.lista_personas, tiempo_total
    cont+= 1


print (f'El usuario ha completado el juevo en un tiempo de {tiempo_total}s')

cont+=1