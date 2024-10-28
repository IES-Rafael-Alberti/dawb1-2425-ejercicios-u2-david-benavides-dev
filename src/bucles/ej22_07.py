# Ejercicio 2.2.7
# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
from utils import *


def tabla_multiplicar_numero(num: int):
    """
    
    """
    tabla_multiplicar = ""
    for i in range(10+1):
        tabla_multiplicar += f"{num} x {i} es: {(i * num)}\n"
    return tabla_multiplicar.rstrip("\n")


def main():
    num = pedir_num("Introduce un número: ")
    print(tabla_multiplicar_numero(num))


if __name__ == "__main__":
    main()