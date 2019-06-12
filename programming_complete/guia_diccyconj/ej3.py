comidas = {"completo": 300, "churrasco": 400, "papas fritas": 200, "especialidad": 1500}

def livianos(n,comidas):
    auxiliar = []
    diccionario = {}
    for nombre,calorias in comidas.items():
        auxiliar.append((calorias,nombre))
    auxiliar.sort()
    for calorias,nombre in auxiliar[:n]:
        diccionario[nombre] = calorias
    return diccionario.items()

def regular(tope,comidas):
    for nombre,calorias in comidas.items():
        if calorias >= tope:
            del comidas[nombre]
    return comidas
    
