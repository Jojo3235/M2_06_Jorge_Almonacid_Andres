#Ejercicio 3

import sys

def pedir_numero(cond):
    while True:
        num=input("{}: ".format(cond))
        try:
            num=float(num)
        except:
            print("El número introducido no es válido", file=sys.stderr)
        else:
            return num

def altura_metros(altura):
    if altura<=3:
        return altura
    else:
        return float(altura/100)
        
def imc():
    pedir_peso=pedir_numero("Introduzca su peso")
    peso=round(float(pedir_peso),2)
    pedir_altura=pedir_numero("Introduzca su altura en metros")
    altura=round(altura_metros(pedir_altura),2)
    indmc = peso/(altura**2)
    indmc_r = round(float(indmc),2)
    if indmc<18.50:
        print("Se encuentra en la zona de bajo peso, su IMC es de: {} Kg/m^2".format(indmc_r))
    elif 18.50<=indmc<25.00:
        print("Se encuentra en la zona de peso normal, su IMC es de: {} Kg/m^2".format(indmc_r))
    elif 25.00<=indmc<30.00:
        print("Se encuentra en la zona de sobrepeso, su IMC es de: {} Kg/m^2".format(indmc_r))
    else:
        print("Se encuentra en la zona de obesidad, su IMC es de: {} Kg/m^2".format(indmc_r))

imc()