# Ejercicio 2.2.22
# Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el 0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene. 
# Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.
from utils import *


def main():
    parar = False

    while parar is False:
        numero = pedir_num("Introduce un número entero positivo: ")

        if numero == 0:
            parar = True


if __name__ == "__main__":
    main()