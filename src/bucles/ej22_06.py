# Ejercicio 2.2.6
# 
# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
# 
# *
# **
# ***
# ****
# *****


def validar_entero(msj: str) -> bool:
    """
    
    """
    try:
        num = int(msj)
        if num >= 0:
            return True
        else:
            return False
    except ValueError:
        return False


def obtener_entero() -> str:
    """
    
    """
    msj = input("Introduce un número entero: ")
    while not validar_entero(msj):
        print("*ERROR** Debes introducir un número entero.")
        msj = input("Introduce nuevamente un número: ")
    return int(msj)


def generar_triangulo_rectangulo(n: int):
    """
    
    """
    for i in range(n):
        print("*" * i)


def main():
    numero = obtener_entero()
    generar_triangulo_rectangulo(numero)


if __name__ == "__main__":
    main()