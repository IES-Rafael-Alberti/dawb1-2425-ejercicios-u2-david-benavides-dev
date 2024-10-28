# Ejercicio 2.2.10
# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
from utils import *


def validar_primo(num) -> bool:
    """
    
    """
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def mostrar_numero(num):
    """
    
    """
    if validar_primo(num):
        return f"El número {num} es primo."
    return f"El número {num} no es primo."


def main():

    num = pedir_num("Introduce un número: ")

    print(mostrar_numero(num))


if __name__ == "__main__":
    main()