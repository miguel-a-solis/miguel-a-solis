def maravillas_seleccionadas(nombre,votacion):
    diccionario = {}
    archivo = open(nombre)
    for linea in archivo:
        datos = linea.strip().split(":")
        maravilla = datos[0].split("/")[-1]
        votos = float(datos[-1])
        if votos >= votacion:
            diccionario[maravilla] = (votos/100)*1600
    archivo.close()
    return diccionario

def suma(nombre,pais):
    total = 0
    archivo = open(nombre)
    for linea in archivo:
        datos = linea.strip().split(":")
        origen = datos[1]
        if origen == pais:
            total += float(datos[-1])
    archivo.close()
    return total
            
        
