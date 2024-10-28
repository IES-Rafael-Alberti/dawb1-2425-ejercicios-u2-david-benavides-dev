# Ejercicio 2.2.3
# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
from utils import *


def mostrar_impares(numero: int) -> str:
    """
    
    """
    serie_numeros = ""

    for i in range(1, numero):
        if i % 2 == 1:
            serie_numeros += f"{i}, "

    return serie_numeros[:-2]


def main():
    numero = pedir_num("Introduce un número entero positivo: ")
    print(mostrar_impares(numero))


if __name__ == "__main__":
    main()