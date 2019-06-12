correos={ 'Jacque Lebrom' : 'jlebrom@francemail.com.fr',
          'Funcionario UNAB' : 'nombre@unab.cl',
          'Daniel Quispe' : 'dquisp@ucsp.com.pe'}

dominios = {'fr' : 'Francia', 'cl' : 'Chile', 'pe' : 'Peru'}

def pais(nombre, correos, dominios):
    correo = correos[nombre]
    dominio = correo.split(".")[-1]
    return dominios[dominio]

def contador(pais, correos, dominios):
    cuenta = 0
    for nombre,correo in correos.items():
        dominio = correo.split(".")[-1]
        if dominios[dominio] == pais:
            cuenta += 1
    return cuenta
