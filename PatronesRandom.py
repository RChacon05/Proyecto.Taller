import random as r

def organizar(l:list):
    """Esta función se encarga de organizar una lista aleatoria para que no hayan números
    repetidos, manteniendo la misma cantidad de números originales.

    Args:
        l (list): lista generada aleatoriamente la cual será modificada.

    Returns:
        list: retorna la lista modificada sin números repetidos.
    """
    while True:
        lFinal:list=[]
        while True:
            lFinal.clear()
            while len(l)>1:
                l.sort()
                if l[0]==l[1]:
                    l.pop(0)
                    lFinal.extend([r.randint(0,4)for i in range(1)])
                else:
                    lFinal.extend(l[:1])
                    l.pop(0)
            lFinal.extend(l)
            lFinal.sort()
            l.clear()
            l+=lFinal
            
            while not lFinal[0]==lFinal[1]:
                lFinal.pop(0)
                if len(lFinal)==1:
                    r.shuffle(l)
                    return l
