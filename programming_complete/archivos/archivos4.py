clientes = [('12.345.678-0', 82556743), ('16.345.543-k', 83287252)]

def cobrar(clientes,rut):
    cobro = 0
    for cliente,numero in clientes:
        if cliente == rut:
            nombre = numero
    archivo = open(str(nombre) + ".txt")
    for linea in archivo:
        linea = linea.strip()
        datos = linea.split()
        cobro += int(datos[-1])*60
    archivo.close()
    return cobro
    
