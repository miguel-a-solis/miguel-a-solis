def empresa(nombre):
    diccionario = {"Empresa X": set(), "Empresa Y": set(), "Empresa Z": set()}
    archivo = open(nombre)
    for linea in archivo:
        datos = linea.strip().split(",")
        numeros = datos[-1].split("-")
        if int(numeros[0])%2 == 0 and int(numeros[0])%3 != 0:
            diccionario["Empresa Y"].add(datos[0])
        elif int(numeros[0])%2 != 0 and int(numeros[0])%3 == 0:
            diccionario["Empresa X"].add(datos[0])
        else:
            diccionario["Empresa Z"].add(datos[0])
    archivo.close()
    return diccionario

def ordenar(nombre):
    archivo = open(nombre)
    for linea in archivo:
        datos = linea.strip().split(",")
        nombre_completo = datos[0].split()
        sin_apellido = " ".join(nombre_completo[:-1])
        pais = datos[1]
        destino = open(pais+".txt", "a")
        destino.write(" ".join([sin_apellido,datos[-1]]) +"\n")
        destino.close()
    archivo.close()
