#Ejercicio 2

import sys      #Importamos las librerias necesarias

def lee_numero(cond):     #Creamos una función para pedir números y que nos los lea
    while True:
        num=input("{}: ".format(cond))
        try:
            num=float(num)
        except:
            print("El número introducido no es válido", file=sys.stderr)
        else:
            return num

def mayor(num1,num2,num3):  #Creamos una función para que nos compare los números
    lista=list()    #Creamos una lista vacía a la que le añadimos números en función de los parámetros introducidos
    lista.append(num1)
    lista.append(num2)
    lista.append(num3)
    return ("El número mayor de los 3 es: {}".format(max(lista)))   #Nos devuelve cual es el mayor de todos

num1=lee_numero("Introduzca un número") 
num2=lee_numero("Introduzca un número")         #Pedimos los números por pantalla
num3=lee_numero("Introduzca un número")

print(mayor(num1,num2,num3))    #Imprimimos cual es el mayor de todos