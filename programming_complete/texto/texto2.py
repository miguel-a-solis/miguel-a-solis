msj1 = "Nombre alumno {0}:"
msj2 = "Notas de {0}:"
msj3 = "El promedio de {nom} es {prom}"
cuenta = 1
lista = []
while True:
    nombre = raw_input(msj1.format(cuenta))
    if nombre.lower() == "fin":
        break
    n = nombre.split()[0]
    notas = raw_input(msj2.format(n))
    lista_notas = notas.split()
    lista_notas = map(float,lista_notas)
    p = round(sum(lista_notas)/len(lista_notas),1)
    lista.append((n,p))
    cuenta += 1
for nombre,promedio in lista:
    print msj3.format(prom = promedio, nom = nombre)
