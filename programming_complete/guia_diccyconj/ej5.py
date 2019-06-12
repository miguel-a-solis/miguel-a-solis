tiempos = {"V": [("Juan",39), ("Roberto",30),("Pedro",38),],
           "RM": [("Mario",40),("Jose",35),("Marcelo",45),("Manuel",42)]}
resultados = [("Roberto",35), ("Pedro",34), ("Mario",36), ("Jose",33)]
def clasificados(region,tiempos):
    conjunto = set()
    auxiliar = []
    for ciclista,tiempo in tiempos[region]:
        auxiliar.append((tiempo,ciclista))
    auxiliar.sort()
    for tiempo,ciclista in auxiliar[:2]:
        conjunto.add(ciclista)
    return conjunto

def clasifica(ciclista,tiempos):
    for region in tiempos:
        if ciclista in clasificados(region,tiempos):
            return True
    return False

def ranking(tiempos,resultados):
    auxiliar = []
    diccionario = {}
    for ciclista,tiempo in resultados:
        auxiliar.append((tiempo,ciclista))
    auxiliar.sort()
    lugar = 1
    for tiempo,ciclista in auxiliar:
        for region in tiempos:
            if ciclista in clasificados(region,tiempos):
                if region not in diccionario:
                    diccionario[region] = []
                diccionario[region].append((ciclista,lugar))
                lugar += 1
    return diccionario
        
