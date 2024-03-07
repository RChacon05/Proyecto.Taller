import time as t
import agenda
from os import system


black   = "\033[0;30m"
red     = "\033[0;31m"
green   = "\033[0;32m"
yellow  = "\033[0;33m"
white   = "\033[0;37m"
nocolor = "\033[0m"

def menu():
  while True:    
    print (chr(27) + "[2J")
    print (green)
    print ("!!Patron de Frutas!!")
    print (yellow)
    print ("\n")
    print ("Iniciar")
    print ("\n",white)
    opt=int(input ("Digite 1 para iniciar el juego: "))
    if opt==1:
      registrar_jugador()        
    else:
      pass
      
  print (chr(27) + "[2J")

def registrar_jugador():
  print (chr(27) + "[2J")
  nombre=input ("ingrese un Jugador: ")
  system("cls")
  agenda.insertar(nombre)
  print("Jugadores:", agenda.lista_personas)
  t.sleep(0.5)
  print (yellow)
  print ("\n")
  print ("1) Agregar otro Jugador")
  print ("2) Jugar")
  print ("\n",white)
  opt=int(input ("Digite alguna de las opciones anteriores: "))
  if opt==1:
      registrar_jugador()        
  elif opt==2:
    import app 
  
    
menu()