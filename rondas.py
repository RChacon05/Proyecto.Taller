import ARMem as ar
import time as t
import colores as co
import utilidades as u

lista_ronda1=[[0][0][0][0][0]]
lista_ronda2=[[0][0][0][0][0]]
lista_ronda3=[[0][0][0][0][0]]

#lista_ronda1=[[0,1,2][2,4,0][3,0,1][1,3,4][4,2,3]]
#lista_ronda2=[[0,1,2,3][2,4,0,1][3,0,1,4][1,3,4,2][4,2,3,0]]
#lista_ronda3=[[0,1,2,3,4][2,4,0,1,3][3,0,1,4,2][1,3,4,2,0][4,2,3,0,1]]

print('\033[2J')  # Código ANSI para limpiar la pantalla en sistemas Windows
tiempo_ronda1=0
tiempo_ronda2=0
tiempo_ronda3=0
print("RONDA 1")
t.sleep(2)
for x in lista_ronda1:
    turno_jugador = 1
    cont=0
    while turno_jugador<= len(u.lista_personas):
        print('\033[2J')
        print(f"turno de:", u.lista_personas[cont])
        t.sleep(3.5)
        print(f'Memorice la siguiente secuencia...')
        print(co.green)
        u.imprimir_frutas(x)
        print(co.blue)
        t.sleep(8)
        print('\033[2J')
        print(f'Ordene los marcadores en el orden que se le indicó!')
        t.sleep(2.5)
        print('\033[2J')  
        tiempo_partida=round(ar.start_sorting(x,flip_image=True,show_images=True, show_coordinates=False, show_ids=False, show_identified_marker=False)  ,2)
        tiempo_ronda1+=tiempo_partida
        print(f'Tiempo de partida: {tiempo_partida}s')
        t.sleep(3)
        print('\033[2J')  
        u.jugadores_turno[u.lista_personas[cont]]= tiempo_partida
        if not(u.lista_personas[cont] in u.jugadores_ronda1):
            u.jugadores_ronda1[u.lista_personas[cont]]= tiempo_ronda1
        else:
            u.jugadores_ronda1[u.lista_personas[cont]]+= tiempo_ronda1
        turno_jugador+= 1
        cont+= 1
    else:
        for J,T in u.jugadores_turno.items():
            print ("El jugador", J,"ha completado el turno en un tiempo de", T,"s")
            t.sleep(1)
        t.sleep(3)

for J,T in u.jugadores_ronda1.items():
    print ("El jugador", J,"ha completado la ronda en un tiempo de", T,"s")
    t.sleep(1)
print("comenzando la siguiente ronda...")
t.sleep(4)
print('\033[2J')
print("RONDA 2")
t.sleep(2)
print('\033[2J')
print(co.red)
print("!!! Mas rapido !!!")
t.sleep(0.5)
print('\033[2J')
t.sleep(0.5)
print("!!! Mas rapido !!!")
t.sleep(0.5)
print('\033[2J')
t.sleep(0.5)
print("!!! Mas rapido !!!")
t.sleep(0.5)
print('\033[2J')
t.sleep(0.5)
print("!!! Mas rapido !!!")
t.sleep(1.5)
print('\033[2J')
print(co.blue)
for x in lista_ronda2:
    turno_jugador = 1
    cont=0
    while turno_jugador<= len(u.lista_personas):
        print('\033[2J')
        print(f"turno de:", u.lista_personas[cont])
        t.sleep(3.5)
        print(f'Memorice la siguiente secuencia...')
        print(co.green)
        u.imprimir_frutas(x)
        print(co.blue)
        t.sleep(6)
        print('\033[2J')
        print(f'Ordene los marcadores en el orden que se le indicó!')
        t.sleep(2.5)
        print('\033[2J')  
        tiempo_partida=round(ar.start_sorting(x,flip_image=True,show_images=True, show_coordinates=False, show_ids=False, show_identified_marker=False)  ,2)
        tiempo_ronda2+=tiempo_partida
        print(f'Tiempo de partida: {tiempo_partida}s')
        t.sleep(3)
        print('\033[2J')  
        u.jugadores_turno[u.lista_personas[cont]]= tiempo_partida
        if not(u.lista_personas[cont] in u.jugadores_ronda2):
            u.jugadores_ronda2[u.lista_personas[cont]]= tiempo_ronda2
        else:
            u.jugadores_ronda2[u.lista_personas[cont]]+= tiempo_ronda2
        turno_jugador+= 1
        cont+= 1
    else:
        for J,T in u.jugadores_turno.items():
            print ("El jugador", J,"ha completado el turno en un tiempo de", T,"s")
            t.sleep(1)
        t.sleep(3)

for J,T in u.jugadores_ronda2.items():
    print ("El jugador", J,"ha completado la ronda en un tiempo de", T,"s")
    t.sleep(1)
print("comenzando la siguiente ronda...")
t.sleep(4)
print('\033[2J')
print("RONDA 3")
t.sleep(2)
print('\033[2J')
print(co.red)
print("!!! Mas rapido !!!")
t.sleep(0.5)
print('\033[2J')
t.sleep(0.5)
print("!!! Mas rapido !!!")
t.sleep(0.5)
print('\033[2J')
t.sleep(0.5)
print("!!! Mas rapido !!!")
t.sleep(0.5)
print('\033[2J')
t.sleep(0.5)
print("!!! Mas rapido !!!")
t.sleep(1.5)
print('\033[2J')
print(co.blue)
for x in lista_ronda3:
    turno_jugador = 1
    cont=0
    while turno_jugador<= len(u.lista_personas):
        print('\033[2J')
        print(f"turno de:", u.lista_personas[cont])
        t.sleep(3.5)
        print(f'Memorice la siguiente secuencia...')
        print(co.green)
        u.imprimir_frutas(x)
        print(co.blue)
        t.sleep(4)
        print('\033[2J')
        print(f'Ordene los marcadores en el orden que se le indicó!')
        t.sleep(2.5)
        print('\033[2J')  
        tiempo_partida=round(ar.start_sorting(x,flip_image=True,show_images=True, show_coordinates=False, show_ids=False, show_identified_marker=False)  ,2)
        tiempo_ronda3+=tiempo_partida
        print(f'Tiempo de partida: {tiempo_partida}s')
        t.sleep(3)
        print('\033[2J')  
        u.jugadores_turno[u.lista_personas[cont]]= tiempo_partida
        if not(u.lista_personas[cont] in u.jugadores_ronda3):
            u.jugadores_ronda3[u.lista_personas[cont]]= tiempo_ronda3
        else:
            u.jugadores_ronda3[u.lista_personas[cont]]+= tiempo_ronda3
        turno_jugador+= 1
        cont+= 1
    else:
        for J,T in u.jugadores_turno.items():
            print ("El jugador", J,"ha completado el turno en un tiempo de", T,"s")
            t.sleep(1)
        t.sleep(3)

for J,T in u.jugadores_ronda3.items():
    print ("El jugador", J,"ha completado la ronda en un tiempo de", T,"s")
    t.sleep(1)
print("Mostrando puntuaciones en breve...")
t.sleep(4)
print("resultado final en 3...")
t.sleep(1)
print("resultado final en 2...")
t.sleep(1)
print("resultado final en 1...")
t.sleep(1)
#aqui va el ranking final xd ordenados del menor a mayor tiempo