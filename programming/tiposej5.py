numero = float(raw_input("Ingrese numero: "))
decimales = numero-int(numero)
decimales_como_letras = str(decimales)[2:]
decimales_en_numeros = int(decimales_como_letras)
print "La parte decimal es", decimales_en_numeros
