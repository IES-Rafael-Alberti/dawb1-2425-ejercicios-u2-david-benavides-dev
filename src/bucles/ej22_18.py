# Ejercicio 2.2.18
# Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. 
# La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.
from utils import *


numero = 0
cont = 0
while numero != -1:
    numero = int(input("NUMBER "))
    if numero % 2 == 0:
        cont += 1

    if numero > 0:
        suma = 0
        for i in range (numero):
            suma += i
        print(suma)


print(F"PARES {cont}")

def main():
    return

if __name__ == "__main__":
    main()