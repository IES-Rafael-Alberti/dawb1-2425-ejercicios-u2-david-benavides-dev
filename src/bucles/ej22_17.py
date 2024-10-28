# Ejercicio 2.2.17
# Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.
from utils import *


def sumar_numeros(numero: int) -> int:
    """
    
    """
    numero_completo = 0
    for i in range(numero):
        numero_completo += i

    return numero_completo


def main():
    numero = pedir_num("Introduce un número: ")

    print(sumar_numeros(numero))

if __name__ == "__main__":
    main()