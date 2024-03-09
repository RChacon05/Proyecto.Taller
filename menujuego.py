import time as t
import agenda as ag



black   = "\033[0;30m"
red     = "\033[0;31m"
blue    = '\033[94m'
green   = "\033[0;32m"
yellow  = "\033[0;33m"
white   = "\033[0;37m"
nocolor = "\033[0m"

def menu():
  while True:
    print ('\033[2J')   
    print (chr(27) + "[2J")
    print (blue)
    print ("!!Patron de Frutas!!")
    print (yellow)
    print ("\n")
    print ("1) Iniciar")
    print ("\n",green)
    opt=int(input ("Digite 1 para iniciar el juego: "))
    if opt==1:
      print (chr(27) + "[2J")
      print (green)
      nombre=input ("ingrese un Jugador: ")
      print ('\033[2J')
      ag.insertar(nombre)
      iniciar_juego()      
    else:
      pass
      
  print (chr(27) + "[2J")

def iniciar_juego():
  print (chr(27) + "[2J")
  print (blue)
  print ("Jugadores:", ag.lista_personas)
  print (yellow)
  print ("\n")
  print ("1) Agregar otro Jugador")
  print ("2) Jugar")
  print ("3) Reglas")
  print ("\n",blue)
  opt=int(input ("Digite alguna de las opciones anteriores: "))
  if opt==1:
    print (chr(27) + "[2J")
    print (green)
    nombre=input ("ingrese un Jugador: ")
    print ('\033[2J')
    ag.insertar(nombre)
    iniciar_juego()        
  elif opt==2:
    import app
  elif opt==3:
    reglas()
  else:
    iniciar_juego()
    

def reglas():
  print (chr(27) + "[2J")
  print (yellow)
  print ("Reglas:")
  print ("aqui va a ir la explicacíon de que trata el juego y como jugarlo xd")
  print ("\n",red)
  print ("1) volver")
  print ("\n",green)
  opt=int(input ("Digite 1 para volver al menú de inicio: "))
  if opt==1:
    iniciar_juego()
  else:
    pass


    
menu()