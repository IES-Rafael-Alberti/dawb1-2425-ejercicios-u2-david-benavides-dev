# Ejercicio 2.2.2
# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
from src.bucles.utils import *


def validar_edad(edad: int) -> bool:
    """
    
    """
    if edad < 0 or edad > 100:
        return False
    return True


def anios_cumplidos(edad: int) -> str:
    """
    
    """
    serie_edad = ""
    for i in range(1, edad+1):
        serie_edad = f"{(serie_edad)} + {i}"
    return serie_edad[3:]


def mostrar_serie_edad(edad) -> str:
    """
    
    """
    serie_edad = anios_cumplidos(edad)
    return f"Para llegar a tu edad actual ({edad}) has tenido que cumplir {serie_edad} años."
    

def main():
    edad = pedir_num("Introduce tu edad: ")

    while validar_edad(edad) is False:
        edad = pedir_num("Introduce una edad correcta: ")

    print(mostrar_serie_edad(edad))


if __name__ == "__main__":
    main()