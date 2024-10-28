# Ejercicio 2.2.14
# Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.
from utils import *


def sumar_numeros_enteros(suma_total: int = 0) -> int:
    """
    
    """
    while True:
        numero = pedir_num("Introduce un número (0 para salir): ")
        suma_total += numero

        if numero == 0:
            return suma_total


def mostrar_sumatoria(sumatoria: int) -> str:
    """
    
    """
    return f"La sumatoria total de números es de {sumatoria}."


def main():
    sumatoria = sumar_numeros_enteros()

    print(mostrar_sumatoria(sumatoria))


if __name__ == "__main__":
    main()