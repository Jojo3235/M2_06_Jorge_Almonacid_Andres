#Ejercicio 3

import sys      #Importamos las librerias necesarias

def pedir_numero(cond):         #Creamos una función para pedir números
    while True:         #Nos devolverá números siempre que se introduzca un número
        num=input("{}: ".format(cond))
        try:
            num=float(num)
        except:
            print("El número introducido no es válido", file=sys.stderr)
        else:
            return num

def altura_metros(altura):      #Creamos una función para que la altura este siempre expresada en metros
    if altura<=3:
        return altura
    else:
        return float(altura/100)

def imc():          #Creamos la función para calcular el IMC
    pedir_peso=pedir_numero("Introduzca su peso")       #Pedimos el peso
    peso=round(float(pedir_peso),2)     #Lo redondeamos a 2 decimales 
    pedir_altura=pedir_numero("Introduzca su altura en metros") #Pedimos la altura
    altura=round(altura_metros(pedir_altura),2) #La redondeamos a 2 decimales
    indmc = peso/(altura**2)        #Definimos la variable indmc según la fórmula del IMC
    indmc_r = round(float(indmc),2)     #Redondeamos el resultado a 2 decimales
    if indmc<18.50:         #Ponemos las condiciones para que devuelva el estado de peso de la persona junto a su IMC
        print("Se encuentra en la zona de bajo peso, su IMC es de: {} Kg/m^2".format(indmc_r))
    elif 18.50<=indmc<25.00:
        print("Se encuentra en la zona de peso normal, su IMC es de: {} Kg/m^2".format(indmc_r))
    elif 25.00<=indmc<30.00:
        print("Se encuentra en la zona de sobrepeso, su IMC es de: {} Kg/m^2".format(indmc_r))
    else:
        print("Se encuentra en la zona de obesidad, su IMC es de: {} Kg/m^2".format(indmc_r))

imc()       #Ejecutamos la función