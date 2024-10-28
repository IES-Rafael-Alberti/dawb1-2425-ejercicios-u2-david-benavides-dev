# Ejercicio 2.2.18
# Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. 
# La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.
from utils import *


def calcular_numeros_pares() -> int:
    """
    
    """
    numero = 0
    cont = 0
    while numero != -1 or numero is 0:
        numero = pedir_num("Ingrese un número: ")
        if numero <= -2:
            print("Número inválido")
            numero = 0
        elif numero % 2 == 0:
            cont += 1

        if numero > 0:
            suma = 0
            for i in range (numero):
                suma += i
            print(f"La suma de los dígitos del número {numero} es {suma}.")
    return cont


def main():
    mostrar_numeros_ingresados = calcular_numeros_pares()

    print (f"Has ingresado un total de {mostrar_numeros_ingresados} números pares.")


if __name__ == "__main__":
    main()