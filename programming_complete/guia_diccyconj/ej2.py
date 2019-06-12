fechas = {"Camilo": (05,10,1984), "Roberto": (15,8,1983),
          "Valentina":(18,04,1992), "Nadia": (9,04,1991)}

def cumple(m, fechas):
    lista = []
    for llave,valor in fechas.items():
        if valor[1] == m:
            lista.append((llave,valor[0]))
    return lista

def edades(f, fechas):
    diccionario = {}
    dhoy,mhoy,ahoy = f
    for llave,valor in fechas.items():
        dnac,mnac,anac = valor
        if (mnac,dnac) <= (mhoy,dhoy):
            diccionario[llave] = ahoy-anac
        else:
            diccionario[llave] = ahoy-anac-1
    return diccionario
