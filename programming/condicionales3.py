a = float(raw_input("a: "))
b = float(raw_input("b: "))
c = float(raw_input("c: "))
D = b**2 - 4*a*c
if D > 0:
    print "Tiene dos soluciones reales y distintas"
elif D == 0:
    print "Tiene dos soluciones reales e iguales"
else:
    print "Tiene dos soluciones complejas"

# Alternativa:
# (borrar '#' y comentar o borrar el codigo anterior)
#
#a = float(raw_input("a: "))
#b = float(raw_input("b: "))
#c = float(raw_input("c: "))
#D = b**2 - 4*a*c
#if D >= 0:
#    if D > 0:
#        print "Tiene dos soluciones reales y distintas"
#    else:
#        print "Tiene dos soluciones reales e iguales"
#else:
#    print "Tiene dos soluciones complejas"
