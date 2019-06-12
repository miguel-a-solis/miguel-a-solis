m = int(raw_input('Cantidad de minutos: '))
h = raw_input('Horario: ')
if h == 'DIA':
    p = m * 10
else:
    p = m * 7
print 'Usted debera pagar', p, 'pesos'
if p >= 1500:
    print 'Con la promocion queda en', int(round(p*0.9)), 'pesos'
else:
    print 'No hay descuento'
