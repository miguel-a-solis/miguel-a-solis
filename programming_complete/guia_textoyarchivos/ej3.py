def analizar(archivos):
    archivo = open(archivos)
    destino = open("infectados.txt","w")
    for linea in archivo:
        linea = linea.strip()
        origen = open(linea)
        for linea2 in origen:
            if "VIRUS" in linea2:
                destino.write(linea+"\n")
        origen.close()
    destino.close()
    archivo.close()

def ordenar(archivos):
    lista = []
    archivo = open(archivos)
    for linea in archivo:
        linea = linea.strip()
        lista.append(linea)
    archivo.close()
    lista.sort()
    destino = open("ordenados.txt","w")
    for nombre in lista:
        destino.write(nombre+"\n")
    destino.close()
    
        
