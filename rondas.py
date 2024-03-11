import ARMem as ar
import time as t
import colores as co
import utilidades as u

lista_nivel1=[[0],[0],[0],[0],[0]]
lista_nivel2=[[0],[0],[0],[0],[0]]
lista_nivel3=[[0],[0],[0],[0],[0]]

#lista_nivel1=[[0,1,2][2,4,0][3,0,1][1,3,4][4,2,3]]
#lista_nivel2=[[0,1,2,3][2,4,0,1][3,0,1,4][1,3,4,2][4,2,3,0]]
#lista_nivel3=[[0,1,2,3,4][2,4,0,1,3][3,0,1,4,2][1,3,4,2,0][4,2,3,0,1]]

print('\033[2J')  # Código ANSI para limpiar la pantalla en sistemas Windows
print("NIVEL 1")
t.sleep(2)
for x in lista_nivel1:
    cont=0
    while cont< len(u.lista_personas):
        print('\033[2J')
        print(f"turno de:", u.lista_personas[cont])
        t.sleep(1.5)
        print(f'Memorice la siguiente secuencia...')
        print(co.green)
        u.imprimir_frutas(x)
        print(co.blue)
        t.sleep(1)
        print('\033[2J')
        print(f'Ordene los marcadores en el orden que se le indicó!')
        t.sleep(1.5)
        print('\033[2J')  
        tiempo_turno=round(ar.start_sorting(x,flip_image=False,show_images=True, show_coordinates=False, show_ids=False, show_identified_marker=False)  ,2)
        tiempo_nivel1+=tiempo_turno
        print(f'Tiempo de partida: {tiempo_turno}s')
        t.sleep(3)
        print('\033[2J')  
        u.jugadores_turno[u.lista_personas[cont]]= tiempo_turno
        if not(u.lista_personas[cont] in u.jugadores_nivel1):
            u.jugadores_nivel1[u.lista_personas[cont]]= tiempo_nivel1
        else:
            u.jugadores_nivel1[u.lista_personas[cont]]+= tiempo_nivel1
        cont+= 1
        tiempo_nivel1= 0
    else:
        for J,T in u.jugadores_turno.items():
            print ("El jugador", J,"ha completado el turno en un tiempo de", T,"s")
            t.sleep(1)
        t.sleep(3)
        print('\033[2J')
for J,T in u.jugadores_nivel1.items():
    print ("El jugador", J,"ha completado la nivel en un tiempo de", T,"s")
    t.sleep(1)
print("comenzando la siguiente nivel...")
t.sleep(4)
print('\033[2J')
print("NIVEL 2")
t.sleep(2)
print('\033[2J')
print(co.red)
print("!!! Cantidad de Frutas Aumentada !!!")
t.sleep(0.5)
print('\033[2J')
t.sleep(0.5)
print("!!! Cantidad de Frutas Aumentada !!!")
t.sleep(0.5)
print('\033[2J')
t.sleep(0.5)
print("!!! Cantidad de Frutas Aumentada !!!")
t.sleep(0.5)
print('\033[2J')
t.sleep(0.5)
print("!!! Cantidad de Frutas Aumentada !!!")
t.sleep(1.5)
print('\033[2J')
print(co.blue)
for x in lista_nivel2:
    cont=0
    while cont< len(u.lista_personas):
        print('\033[2J')
        print(f"turno de:", u.lista_personas[cont])
        t.sleep(3.5)
        print(f'Memorice la siguiente secuencia...')
        print(co.green)
        u.imprimir_frutas(x)
        print(co.blue)
        t.sleep(5)
        print('\033[2J')
        print(f'Ordene los marcadores en el orden que se le indicó!')
        t.sleep(2.5)
        print('\033[2J')  
        tiempo_turno=round(ar.start_sorting(x,flip_image=True,show_images=True, show_coordinates=False, show_ids=False, show_identified_marker=False)  ,2)
        tiempo_nivel2+=tiempo_turno
        print(f'Tiempo de partida: {tiempo_turno}s')
        t.sleep(3)
        print('\033[2J')  
        u.jugadores_turno[u.lista_personas[cont]]= tiempo_turno
        if not(u.lista_personas[cont] in u.jugadores_nivel2):
            u.jugadores_nivel2[u.lista_personas[cont]]= tiempo_nivel2
        else:
            u.jugadores_nivel2[u.lista_personas[cont]]+= tiempo_nivel2
        cont+= 1
        tiempo_nivel2=0
    else:
        for J,T in u.jugadores_turno.items():
            print ("El jugador", J,"ha completado el turno en un tiempo de", T,"s")
            t.sleep(1)
        t.sleep(3)
        print('\033[2J')
for J,T in u.jugadores_nivel2.items():
    print ("El jugador", J,"ha completado la nivel en un tiempo de", T,"s")
    t.sleep(1)
print("comenzando la siguiente nivel...")
t.sleep(4)
print('\033[2J')
print("NIVEL 3")
t.sleep(2)
print('\033[2J')
print(co.red)
print("!!! Cantidad de Frutas Aumentada !!!")
t.sleep(0.5)
print('\033[2J')
t.sleep(0.5)
print("!!! Cantidad de Frutas Aumentada !!!")
t.sleep(0.5)
print('\033[2J')
t.sleep(0.5)
print("!!! Cantidad de Frutas Aumentada !!!")
t.sleep(0.5)
print('\033[2J')
t.sleep(0.5)
print("!!! Cantidad de Frutas Aumentada !!!")
t.sleep(1.5)
print('\033[2J')
print(co.blue)
for x in lista_nivel3:
    cont=0
    while cont< len(u.lista_personas):
        print('\033[2J')
        print(f"turno de:", u.lista_personas[cont])
        t.sleep(3.5)
        print(f'Memorice la siguiente secuencia...')
        print(co.green)
        u.imprimir_frutas(x)
        print(co.blue)
        t.sleep(5)
        print('\033[2J')
        print(f'Ordene los marcadores en el orden que se le indicó!')
        t.sleep(2.5)
        print('\033[2J')  
        tiempo_turno=round(ar.start_sorting(x,flip_image=True,show_images=True, show_coordinates=False, show_ids=False, show_identified_marker=False)  ,2)
        tiempo_nivel3+=tiempo_turno
        print(f'Tiempo de partida: {tiempo_turno}s')
        t.sleep(3)
        print('\033[2J')  
        u.jugadores_turno[u.lista_personas[cont]]= tiempo_turno
        if not(u.lista_personas[cont] in u.jugadores_nivel3):
            u.jugadores_nivel3[u.lista_personas[cont]]= tiempo_nivel3
        else:
            u.jugadores_nivel3[u.lista_personas[cont]]+= tiempo_nivel3
        cont+= 1
        tiempo_nivel3=0
    else:
        for J,T in u.jugadores_turno.items():
            print ("El jugador", J,"ha completado el turno en un tiempo de", T,"s")
            t.sleep(1)
        t.sleep(3)
        print('\033[2J')
for J,T in u.jugadores_nivel3.items():
    print ("El jugador", J,"ha completado la nivel en un tiempo de", T,"s")
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