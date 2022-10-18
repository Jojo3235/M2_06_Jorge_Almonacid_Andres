import sys
import math as ma


#Ejercicio 1

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


#Ejercicio 2

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

#Ejercicio 3

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