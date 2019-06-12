anho = int(raw_input("Ingrese anho: "))
if anho%4 == 0:
    if anho%100 == 0 and anho%400 != 0:
        print anho,"no es bisiesto"
    else:
        print anho,"es bisiesto"
else:
    print anho,"no es bisiesto"

# Alternativa 1:
# (borrar '#' y comentar o borrar el codigo anterior)
#
#anho = int(raw_input("Ingrese anho: "))
#if anho%4 != 0 or (anho%100 == 0 and anho%400 != 0):
#        print anho,"no es bisiesto"
#else:
#        print anho,"es bisiesto"
# Alternativa 2:
# (borrar '#' y comentar o borrar los codigos anteriores)
#
#anho = int(raw_input("Ingrese anho: "))
#print anho,
#if anho%4 == 0:
#    if anho%100 == 0 and anho%400 != 0:
#        print "no",
#else:
#    print "no",
#print "es bisiesto"        
