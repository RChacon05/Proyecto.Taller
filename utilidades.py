nombre_frutas=["piña","cereza","uva","pera","guanabana"]

def imprimir_frutas(l:list):
    orden_frutas=""
    for e in l:
        orden_frutas+=nombre_frutas[e]+" "
    print(orden_frutas)

jugadores_tiempo={}
lista_personas=[]
def insertar (nombre:str)->None:
  """_summary_

  Args:
      nombre (str): _description_
  """
  lista_personas.append((nombre))
