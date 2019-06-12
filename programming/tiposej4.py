anho = int(raw_input("Ingrese anho: "))
ultimo_par_digitos = anho%100
penultimo_digito = ultimo_par_digitos/10
print "Pertenece a la decada",penultimo_digito + 1

# Alternativa:
# (borrar '#' y comentar o borrar el codigo anterior)
#
#anho = raw_input("Ingrese anho: ")
#penultima_letra = anho[-2]
#penultimo_digito = int(penultima_letra)
#print "Pertenece a la decada",penultimo_digito + 1
