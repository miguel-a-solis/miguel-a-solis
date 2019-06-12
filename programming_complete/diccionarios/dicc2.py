sintonia = {"Lunes":["CHV","MEGA"], "Martes":["TVN","MEGA"],"Miercoles":["CHV"],
            "Jueves":["13"],"Viernes":["CHV","TVN"],"Sabado":["13","MEGA","TVN"],
            "Domingo":["CHV","MEGA"]}

def rating(sintonia):
    diccionario = {}
    for llave,valor in sintonia.items():
        for canal in valor:
            if canal not in diccionario:
                diccionario[canal] = 0
            diccionario[canal] += 1
    return diccionario
