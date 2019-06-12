def contar_letras(palabra):
    diccionario = {}
    for letra in palabra:
        if letra not in diccionario:
            diccionario[letra] = 1
        else:
            diccionario[letra] += 1
    return diccionario
# Alternativa 1:
# (borrar '#' y comentar o borrar el codigo anterior)
#
#def contar_letras(palabra):
#    diccionario = {}
#    for letra in palabra:
#        if letra not in diccionario:
#            diccionario[letra] = 0
#        diccionario[letra] += 1
#    return diccionario
# Alternativa 2:
# (borrar '#' y comentar o borrar el codigo anterior)
#
#def contar_letras(palabra):
#    diccionario = {}
#    for letra in palabra:
#        if letra not in diccionario:
#            diccionario[letra] = palabra.count(letra)
#    return diccionario
