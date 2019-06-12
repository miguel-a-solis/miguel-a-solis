def letras_comun(s1,s2):
    contador = 0
    agregadas = set()
    for letra in s1:
        for letra2 in s2:
            if letra == letra2 and letra not in agregadas:
                agregadas.add(letra)
                contador += 1
    return contador

# Alternativa 1:
# (borrar '#' y comentar o borrar el codigo anterior)
#
#def letras_comun(s1,s2):
#    return len(set(s1)&set(s2))
