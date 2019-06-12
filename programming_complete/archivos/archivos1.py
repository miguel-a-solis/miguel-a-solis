def contar(nombre):
    diccionario = {}
    archivo = open(nombre)
    for linea in archivo:
        linea = linea.strip().lower()
        lista = linea.split()
        for palabra in lista:
            if palabra not in diccionario:
                diccionario[palabra] = 0
            diccionario[palabra] += 1
    archivo.close()
    return diccionario
