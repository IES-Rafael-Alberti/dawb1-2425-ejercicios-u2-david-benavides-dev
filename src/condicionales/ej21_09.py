# Ejercicio 2.1.9
# 
# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. 
# El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. 
# Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.
from utils import *


def validar_edad(edad: int) -> bool:
    if edad <= 0 or edad > 100:
        return False
    return True


def pedir_edad(msj: str):
    edad = pedir_num(msj)

    while validar_edad(edad) is False:
        edad = pedir_num("Introduce una edad correcta: ")

    return edad


def calcular_precio(edad: int) -> float:
    if edad < 4:
        return 0
    elif 4 <= edad < 18:
        return 5
    return 10


def mostrar_precio(edad: int, precio: float) -> str:
    return f"Al tener {edad} años, tu entrada cuesta: {precio:.2f} €."


def main():
    edad = pedir_edad("Introduce tu edad")
    
    precio = calcular_precio(edad)

    print(mostrar_precio(edad, precio))

if __name__ == "__main__":
    main()