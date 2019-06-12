s1 = float(raw_input('Solemne 1: '))
s2 = float(raw_input('Solemne 2: '))
s3 = float(raw_input('Solemne 3: '))
ph = float(raw_input('Hito proyecto: '))
pf = float(raw_input('Proyecto final: '))
lab = float(raw_input('Laboratorio: '))
np = (s1*0.2 + s2*0.2 + s3*0.2 + ph*0.1 + pf*0.2 + lab*0.2)
np = round(np,1)
print 'Su nota de presentacion es',np
if np >= 5.0 and not (s1 < 4.0 and s2 < 4.0 and pa < 4.0 and pf < 4.0 and lab < 4.0):
    print 'Eximido'
else:
    print 'No eximido'
