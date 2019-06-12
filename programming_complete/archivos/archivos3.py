msjfinal = "{nom}:{prom}\n"
origen = open("notas.txt")
destino = open("alumnos.txt","w")
for linea in origen:
    datos = linea.strip().split("->")
    nombre_completo = datos[0].split()
    n = nombre_completo[0]
    notas = datos[1]
    lista_notas = notas.split()
    lista_notas = map(float,lista_notas)
    promedio = sum(lista_notas)/len(lista_notas)
    promedio = round(promedio,1)
    destino.write(msjfinal.format(nom=n,prom=promedio))
destino.close()
origen.close()
    
