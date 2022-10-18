#Ejercicio 1

import sys          
import math as ma           #Importamos las librerias necesarias

def pedir_numero(cond):          #Creamos una función para pedir un número
    while True:             
        num=input("{}: ".format(cond))
        try:                                    #Mientras no se introduzca un número se seguirá ejecutando
            num=float(num)
        except:
            print("El número introducido no es válido", file=sys.stderr)
        else:
            return num              #Una vez se introduce un número te devuelve el número

def area_circulo():         #Creamos la función para calcular el área del círculo
    r=pedir_numero("Introduzca la longitud del radio para calcular el área del círculo")    #Pedimos el radio usando la función anterior
    pi=ma.pi        #Definimos una variable como pi con la libreria math 
    area=pi*(r**2)      #Definimos la variable del área
    print("El area del círculo es de aproximadamente {} unidades".format(round(area,2)))   #Hacemos que imprima el resultado final redondeado a dos decimales

area_circulo()      #Ejecutamos la función