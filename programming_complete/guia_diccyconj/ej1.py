usuarios = { "Tom Cruise" : { "simpatico" , "comprensivo" } ,
             "Scarlett Johansson" : { "buena onda" , "atletica"} ,
             "Brad Pitt" : { "comprensivo"} }

def buscar(cualidades,usuarios):
    lista = []
    for llave,valor in usuarios.items():
        if cualidades <= valor:
            lista.append(llave)
    return lista

def compatible(persona,cualidades,usuarios):
    mayor = 0
    for llave,valor in usuarios.items():
        if len(cualidades&valor) >= mayor:
            mayor = 100.0*len(cualidades&valor)/len(valor)
            nombre = llave
    return (nombre,mayor)
