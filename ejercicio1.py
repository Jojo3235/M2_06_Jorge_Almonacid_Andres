#Ejercicio 1

import sys
import math as ma

def pedir_numero(cond):
    while True:
        num=input("{}: ".format(cond))
        try:
            num=float(num)
        except:
            print("El número introducido no es válido", file=sys.stderr)
        else:
            return num

def area_circulo():
    r=pedir_numero("Introduzca la longitud del radio para calcular el área del círculo")
    pi=ma.pi
    area=pi*(r**2)
    return round(area,2)

print("El area del círculo es de aproximadamente {} unidades".format(area_circulo()))