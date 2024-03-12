import ARMem as ar
import rank as RK
import random as r
import time as t
import colores as co
import utilidades as u
import PatronesRandom as PR

def reset(f):
     f.finalOrdenado.clear
     f.listaFI.clear
     f.listaFK.clear
     f.resultadoFinal.clear

def juego():
    lista_nivel1=[PR.organizar([r.randint(0,4)for i in range(2)]),PR.organizar([r.randint(0,4)for i in range(3)]),PR.organizar([r.randint(0,4)for i in range(3)]),PR.organizar([r.randint(0,4)for i in range(3)]),PR.organizar([r.randint(0,4)for i in range(3)])]
    lista_nivel2=[PR.organizar([r.randint(0,4)for i in range(2)]),PR.organizar([r.randint(0,4)for i in range(4)]),PR.organizar([r.randint(0,4)for i in range(4)]),PR.organizar([r.randint(0,4)for i in range(4)]),PR.organizar([r.randint(0,4)for i in range(4)])]
    lista_nivel3=[PR.organizar([r.randint(0,4)for i in range(2)]),PR.organizar([r.randint(0,4)for i in range(5)]),PR.organizar([r.randint(0,4)for i in range(5)]),PR.organizar([r.randint(0,4)for i in range(5)]),PR.organizar([r.randint(0,4)for i in range(5)])]
    tiempo_nivel1=0
    tiempo_nivel2=0
    tiempo_nivel3=0

    print('\033[2J')  # Código ANSI para limpiar la pantalla en sistemas Windows
    print("NIVEL 1")
    t.sleep(2)

    for x in lista_nivel1:
            cont=0
            while cont< len(u.lista_personas):
                r.shuffle(x)
                print('\033[2J')
                print(f"turno de:", u.lista_personas[cont])
                t.sleep(3.5)
                print(f'Memorice la siguiente secuencia...')
                print(co.green)
                u.imprimir_frutas(x)
                x.reverse()
                print(co.blue)
                t.sleep(5)
                print('\033[2J')
                print(f'Ordene los marcadores en el orden que se le indicó!')
                t.sleep(2.5)
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
    RK.ranked(u.jugadores_nivel1)    
    min_valor = float('inf')
    for persona, valor in u.jugadores_nivel1.items():
        if valor < min_valor:
            min_valor = valor
            persona_min = persona
    tiempo_nivel1={persona_min,min_valor}
    print('\033[2J')
    print(co.green)
    print(f"{persona_min} es el ganador de el Nivel 1, con un tiempo de ({min_valor}).")
    t.sleep(5)

    print("comenzando el siguiente nivel...")
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
                r.shuffle(x)
                print('\033[2J')
                print(f"turno de:", u.lista_personas[cont])
                t.sleep(3.5)
                print(f'Memorice la siguiente secuencia...')
                print(co.green)
                u.imprimir_frutas(x)
                x.reverse()
                print(co.blue)
                t.sleep(5)
                print('\033[2J')
                print(f'Ordene los marcadores en el orden que se le indicó!')
                t.sleep(2.5)
                print('\033[2J')  
                tiempo_turno=round(ar.start_sorting(x,flip_image=False,show_images=True, show_coordinates=False, show_ids=False, show_identified_marker=False)  ,2)
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
    RK.ranked(u.jugadores_nivel2)
    min_valor = float('inf')
    for persona, valor in u.jugadores_nivel2.items():
        if valor < min_valor:
            min_valor = valor
            persona_min = persona
    tiempo_nivel2={persona_min,min_valor}
    print('\033[2J')
    print(co.green)
    print(f"{persona_min} es el ganador de el Nivel 2, con un tiempo de ({min_valor}).")
    t.sleep(5)

    print("comenzando el siguiente nivel...")
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
            r.shuffle(x)
            print('\033[2J')
            print(f"turno de:", u.lista_personas[cont])
            t.sleep(3.5)
            print(f'Memorice la siguiente secuencia...')
            print(co.green)
            u.imprimir_frutas(x)
            x.reverse()
            print(co.blue)
            t.sleep(5)
            print('\033[2J')
            print(f'Ordene los marcadores en el orden que se le indicó!')
            t.sleep(2.5)
            print('\033[2J')  
            tiempo_turno=round(ar.start_sorting(x,flip_image=False,show_images=True, show_coordinates=False, show_ids=False, show_identified_marker=False)  ,2)
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
    RK.ranked(u.jugadores_nivel3)
    min_valor = float('inf')
    for persona, valor in u.jugadores_nivel3.items():
        if valor < min_valor:
            min_valor = valor
            persona_min = persona
    tiempo_nivel3={persona_min,min_valor}
    print('\033[2J')
    print(co.green)
    print(f"{persona_min} es el ganador de el Nivel 3, con un tiempo de ({min_valor}).")
    t.sleep(5)
    print ('\033[2J')
    print("Mostrando puntuaciones en breve...")
    t.sleep(3)
    print("resultado final en 3...")
    t.sleep(1)
    print("resultado final en 2...")
    t.sleep(1)
    print("resultado final en 1...")
    t.sleep(1)
    resultadoFinal = {}
    for e in u.jugadores_nivel1:
        resultadoFinal[e] = u.jugadores_nivel1[e] + u.jugadores_nivel2[e] + u.jugadores_nivel3[e]
    finalOrdenado = dict(sorted(resultadoFinal.items(), key=lambda item: item[1]))
    listaFK=list(finalOrdenado.keys())
    listaFI=list(finalOrdenado.values())        
    if len(finalOrdenado)>2:
            t.sleep(2)
            print('\033[2J')
            print(co.red)
            print("!!!  TOP 3 !!!")
            t.sleep(2)
            print(f"{ listaFK[2]} con un tiempo de { listaFI[2]}")
            t.sleep(3)
            print(co.green)
            print("!!!  TOP 2 !!!")
            t.sleep(2)
            print(f"{ listaFK[1]} con un tiempo de { listaFI[1]}")
            t.sleep(3)
            print(co.yellow)
            print("!!! 👑 TOP 1 👑!!!")
            t.sleep(2)
            print(f"{ listaFK[0]} con un tiempo de { listaFI[0]}")
    elif len(finalOrdenado)==2:
            t.sleep(2)
            print('\033[2J')
            print(co.yellow)
            print("!!!  TOP 2 !!!")
            t.sleep(2)
            print(f"{ listaFK[1]} con un tiempo de { listaFI[1]}")
            t.sleep(3)
            print(co.yellow)
            print("!!! 👑 TOP 1 👑!!!")
            t.sleep(2)
            print(f"{ listaFK[0]} con un tiempo de { listaFI[0]}")
    elif len(finalOrdenado)<2:
            t.sleep(2)
            print('\033[2J')
            print(co.green)
            print("!!! 👑 TOP 1 👑!!!")
            t.sleep(2)
            print(f"{ listaFK[0]} con un tiempo de { listaFI[0]}")
    t.sleep(5)
    print("\n")
    print(co.blue)
    print("1) Salir")
    print("2) volver a jugar")
    opt=int(input("Digite alguna de las opciones anteriores para continuar: "))
    if opt==1:
         print ('\033[2J')
         print("¡Gracias por jugar! ;)")
         t.sleep(5)
         exit()
    elif opt==2:
         reset(juego())
         juego()

juego()