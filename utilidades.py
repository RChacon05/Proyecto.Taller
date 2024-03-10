nombre_frutas=["piña","cereza","uva","pera","guanabana"]
jugadores_turno={}
jugadores_ronda1={}
jugadores_ronda2={}
jugadores_ronda3={}
lista_personas=[]

def imprimir_frutas(lista:list):
    orden_frutas=""
    for e in lista:
        orden_frutas+=nombre_frutas[e]+" "
    print(orden_frutas)

def insertar (nombre:str)->None:
  """_summary_

  Args:
      nombre (str): _description_
  """
  lista_personas.append((nombre))
