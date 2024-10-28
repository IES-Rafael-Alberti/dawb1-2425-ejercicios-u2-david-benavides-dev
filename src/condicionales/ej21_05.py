# Ejercicio 2.1.5
# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. 
# Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
from utils import *


def validar_edad(edad: int) -> bool:
    """
    
    """
    if edad >= 16:
        return True
    return False


def validar_ingreso(ingresos: float) -> bool:
    """
    
    """
    if ingresos >= 1000:
        return True
    return False


def main():
    """
    
    """
    edad = validar_edad(pedir_num("Introduce tu edad: "))
    ingresos = validar_ingreso(pedir_float("Introduce tus ingresos mensuales: "))

    if edad and ingresos:
        print("Tributas")
    else:
        print("No tributas")


if __name__ == "__main__":
    main()