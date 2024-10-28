# Ejercicio 2.1.7
# Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
# Renta 	Tipo impositivo
# Menos de 10000€ 	5%
# Entre 10000€ y 20000€ 	15%
# Entre 20000€ y 35000€ 	20%
# Entre 35000€ y 60000€ 	30%
# Más de 60000€ 	45%
# Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
from utils import *


nivel_1 = [9999, '5%']
nivel_2 = [10000, 19999, '15%']
nivel_3 = [20000, 34999, '20%']
nivel_4 = [35000, 59999, '30%']
nivel_5 = [60000, '45%']


def calcular_impositivo(impuesto: float) -> str:
    """
    
    """
    if impuesto <= nivel_1[0]:
        impositivo = nivel_1[1]
    elif nivel_2[0] <= impuesto <= nivel_2[1]:
        impositivo = nivel_2[2]
    elif nivel_3[0] <= impuesto <= nivel_3[1]:
        impositivo = nivel_3[2]
    elif nivel_4[0] <= impuesto <= nivel_4[1]:
        impositivo = nivel_4[2]
    elif impuesto >= nivel_5[0]:
        impositivo = nivel_5[1]
    return impositivo


def mostrar_renta(impuesto: float) -> str:
    """
    
    """
    return f"Para tu renta anual de {impuesto:.2f} € le corresponde un tipo de impositivo del {calcular_impositivo(impuesto)}."


def main():
    impuesto = pedir_float("Introduce tu renta anual: ")
    print(mostrar_renta(impuesto))


if __name__ == "__main__":
    main()