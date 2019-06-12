def contar(string):
    diccionario = {}
    lista = string.replace(",","").replace(".","").split()
    for palabra in lista:
        if palabra not in diccionario:
            diccionario[palabra] = 0
        diccionario[palabra] += 1
    return diccionario
