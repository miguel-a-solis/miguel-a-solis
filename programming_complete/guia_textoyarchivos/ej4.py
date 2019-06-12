def mayor(personas,anno):
    archivo = open(personas)
    destino = open("mayores.txt","w")
    for linea in archivo:
        datos = linea.strip().split(":")
        fecha = datos[-1].split("/")
        a = int(fecha[-1])
        edad = anno - a
        if edad >= 18:
            final = [datos[0],str(edad)]
            destino.write("-".join(final)+"\n")
    destino.close()

def ordenar(personas):
    lista = []
    archivo = open(personas)
    destino = open("ordenados.txt","w")
    for linea in archivo:
        datos = linea.strip().split(":")
        nombre_completo = datos[0].split()
        apellido = nombre_completo[-1]
        lista.append((apellido,nombre_completo[0],linea))
    archivo.close()
    lista.sort()
    for apellido,nombre,contenido in lista:
        destino.write(contenido)
    destino.close()
