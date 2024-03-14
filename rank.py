def ranked(l:dict):
    """Función encargada de ordenar los elementos de un diccionario de menor a mayor
    en base al tiempo logardo por cada jugador.

    Args:
        l (dict): Diccionario que será modificado.
    """
    l = dict(sorted(l.items(), key=lambda item: item[1]))
    for persona,valor in l.items():
        print(f"El jugador {persona} ha completado el nivel con un tiempo de {valor}s")




