# Ejercicio 2.2.21
# Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), 
# cortando el ingreso de datos cuando el usuario ingrese el monto 0. Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. 
# Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.
from utils import *


def recibir_monto(msj: str) -> float:
    """
    
    """
    validar_monto = None
    monto = 0

    while validar_monto is None:
        monto_input = pedir_num(msj)

        if monto_input == 0:
            validar_monto = True
            return monto

        elif monto_input < 0:
            validar_monto = None
            input("Por favor, debes introducir un monto mayor que 0.")
        monto += monto_input


def calcular_monto(monto: int) -> int:
    """
    
    """
    if monto >= 1000:
        monto += (monto * 0.10)
        return monto
    return monto


def main():
    monto = recibir_monto("Introduce el monto: ")
    monto_total = calcular_monto(monto)
    print(f"Tu monto total es de {monto_total:.2f} €.")


if __name__ == "__main__":
    main()