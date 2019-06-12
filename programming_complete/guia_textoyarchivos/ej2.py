valores = {'menor': 1200, 'adulto': 2000, 'pensionado': 1500}

def ingresos(fecha):
    total = 0
    fecha = map(str,fecha)
    fecha = "-".join(fecha)
    archivo = open("clientes.txt")
    for linea in archivo:
        datos = linea.strip().split(":")
        if datos[-1] == fecha:
            if int(datos[-2]) < 18:
                total += valores["menor"]
            elif int(datos[-2]) <= 65:
                total += valores["adulto"]
            else:
                total += valores["pensionado"]
    archivo.close()
    return total

def clientes_frecuentes(n):
    diccionario = {}
    lista = []
    archivo = open("clientes.txt")
    for linea in archivo:
        datos = linea.strip().split(":")
        nombre_completo = " ".join(datos[:-2])
        if nombre_completo not in diccionario:
            diccionario[nombre_completo] = 0
        diccionario[nombre_completo] += 1
    archivo.close()
    for nombre, cantidad in diccionario.items():
        if cantidad >= n:
            lista.append(nombre)
    return lista
