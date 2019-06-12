msj1 = "Nombre alumno {0}:"
msj2 = "Notas de {0}:"
msjfinal = "{nom}:{prom}\n"
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
    promedio = sum(lista_notas)/len(lista_notas)
    promedio = round(promedio,1)
    lista.append((n,promedio))
    cuenta += 1
archivo = open("alumnos.txt","w")
for nombre,promedio in lista:
    archivo.write(msjfinal.format(nom=nombre,prom=promedio))
archivo.close()
    
