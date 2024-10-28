# Ejercicio 2.2.8
# 
# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
# 
# 1
# 3 1
# 5 3 1
# 7 5 3 1
# 9 7 5 3 1
from utils import *


def mostrar_triangulo_rectangulo_numeros(num: int):
    """
    
    """
    serie = ""
    cont = 1
    while cont <= num:
        serie = f"{cont} " + serie
        print (serie)
        cont +=2


def main():
    num = pedir_num("Introduce un número: ")
    mostrar_triangulo_rectangulo_numeros(num)


if __name__ == "__main__":
    main()