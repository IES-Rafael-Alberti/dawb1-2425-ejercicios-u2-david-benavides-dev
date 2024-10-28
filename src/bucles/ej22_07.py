# Ejercicio 2.2.7
# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
from utils import *


def tabla_multiplicar_numero(num: int):
    """
    
    """
    for i in range(10):
        print(f"{num} x {i} es: {(i * num)}")


def main():
    """
    
    """
    num = pedir_num("Introduce un número: ")
    tabla_multiplicar_numero(num)


if __name__ == "__main__":
    main()