import time as t
import utilidades as u
import colores as co

def menu():
  while True:
    print ('\033[2J')   
    print (chr(27) + "[2J")
    print (co.blue)
    print ("!!Patron de Frutas!!")
    print (co.yellow)
    print ("\n")
    print ("1) Iniciar")
    print ("\n",co.green)
    opt=int(input ("Digite 1 para iniciar el juego: "))
    if opt==1:
      print (chr(27) + "[2J")
      print (co.green)
      nombre=input ("ingrese un Jugador: ")
      print ('\033[2J')
      u.insertar(nombre)
      iniciar_juego()      
    else:
      pass
      
  print (chr(27) + "[2J")

def iniciar_juego():
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
    import app
  elif opt==3:
    reglas()
  else:
    iniciar_juego()
    

def reglas():
  print (chr(27) + "[2J")
  print (co.yellow)
  print ("Reglas:")
  print ("aqui va a ir la explicacíon de que trata el juego y como jugarlo xd")
  print ("\n",co.red)
  print ("1) volver")
  print ("\n",co.green)
  opt=int(input ("Digite 1 para volver al menú de inicio: "))
  if opt==1:
    iniciar_juego()
  else:
    pass


    
menu()