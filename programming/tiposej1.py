detergentes = int(raw_input("Detergentes comprados: "))
galletas = int(raw_input("Galletas compradas: "))
abarrotes = int(raw_input("Abarrotes comprados: "))

precio_detergentes = 1300
precio_galletas = 500
precio_abarrotes = 800

total = detergentes*precio_detergentes + galletas*precio_galletas + abarrotes*precio_abarrotes

print "Debe pagar",total,"pesos"

# Alternativa:
# (borrar '#' y comentar o borrar el codigo anterior)
#
# d = int(raw_input("Detergentes comprados: "))
# g = int(raw_input("Galletas compradas: "))
# a = int(raw_input("Abarrotes comprados: "))
# print "Debe pagar",d*1300 + g*500 + a*800, "pesos"
