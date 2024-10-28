# Ejercicio 2.2.16
# Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.
from utils import *


def mostrar_numero_mayor():
    numero = pedir_num("Introduce un número: ")
    numero_mayor = numero
    while numero != 0:
        numero = pedir_num("Introduce otro número: ")
        if numero > numero_mayor:
            numero_mayor = numero
    return numero_mayor


def main():
    numero_mayor = mostrar_numero_mayor()

    print(f"El número mayor introducido es: {numero_mayor}")


if __name__ == "__main__":
    main()