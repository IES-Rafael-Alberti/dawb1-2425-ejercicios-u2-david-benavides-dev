# Ejercicio 2.2.5
# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
# 
# # Formula para calcular El capital tras un año.
# amount *= 1 + interest / 100
# # En donde:
# # - amount: Cantidad a invertir
# # - interest: Interes porcentual anual 
from utils import *


def calcular_capital(cantidad: float, interes: float, numero_anios: int):
    """
    
    """
    for i in range(1, numero_anios+1):
        cantidad *= (1 + interes / 100)
        print(f"Año {i}: {cantidad:.2f} €")


def main():
    cantidad = pedir_float("Cantidad a invertir: ")
    interes = pedir_float("Interés anual: ")
    numero_anios = pedir_num("Número de años: ")

    calcular_capital(cantidad, interes, numero_anios)


if __name__ == "__main__":
    main()