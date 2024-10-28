# Ejercicio 2.2.24
# Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, finalizando cuando se reciba un cero.
# Imprimir la cantidad de números primos ingresados.
from utils import *


def pedir_numeros(msj: str) -> list:
    """
    
    """
    lista_numeros = []

    num = pedir_num(msj)
    while num != 0:
        if num > 1:
            lista_numeros.append(num)
        num = pedir_num(msj)

    return lista_numeros


def es_primo(numero: int) -> bool:
    """
    
    """
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False

    return True


def contar_numeros_primos(lista_numeros: list) -> int:
    """
    
    """
    numeros_primos = 0

    for numero in lista_numeros:
        if es_primo(numero):
            numeros_primos += 1

    return numeros_primos


def mostrar_datos(lista_numeros, numeros_primos: int) -> str:
    """
    
    """
    str_numeros = ""

    for numero in lista_numeros:
        str_numeros += f"{numero}, "

    return f"Entre todos los números introducidos ({str_numeros[:-2]}) hay una cantidad de {numeros_primos} numeros primos."


def main():
    numeros = pedir_numeros("Introduce números: ")
    numeros_primos = contar_numeros_primos(numeros)

    print(mostrar_datos(numeros, numeros_primos))


if __name__ == "__main__":
    main()