#Ejercicio 2

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

def lee_numero():
    num=pedir_numero("Introduzca un número")
    return num

def mayor(num1,num2,num3):
    lista=list()
    lista.append(num1)
    lista.append(num2)
    lista.append(num3)
    return ("El número mayor de los 3 es: {}".format(max(lista)))

num1=lee_numero()
num2=lee_numero()
num3=lee_numero()

print(mayor(num1,num2,num3))