precios = { "aceite" : 500 , "arroz" : 2000 , "cafe" : 1500 , "te" : 300 }

def producto_mas_caro(precios):
    mayor = 0
    for nombre,monto in precios.items():
        if monto >= mayor:
            mayor = monto
            caro = nombre
    return caro

def monto_total(precios,compra):
    total = 0
    for producto,cantidad in compra.items():
        total += cantidad*precios[producto]
    return total
