def ranked(l:dict):
    sorted_l = dict(sorted(l.items(), key=lambda item: item[1]))
    for persona,valor in sorted_l.items():
        print(f"el jugador {persona} tiene un tiempo de {valor}")




