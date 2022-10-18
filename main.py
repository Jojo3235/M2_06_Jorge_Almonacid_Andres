import sys
import math as ma


#Ejercicio 1

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


#Ejercicio 2

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

#Ejercicio 3

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