# Ejercicio 2.2.19
# Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 3-finalizar programa. A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3). 
# Si elige una opción incorrecta, informarle del error. El menú se debe volver a mostrar luego de ejecutada cada opción, permitiendo volver a elegir. 
# Si elige las opciones 1 ó 2 se imprimirá un texto. Si elige la opción 3, se interrumpirá la impresión del menú y el programa finalizará.
from utils import *


OPCIONES_VALIDAS = 1, 2, 3


def mostrar_menu():
    """
    
    """
    print("1- comenzar programa")
    print("2- imprimir listado")
    print("3- finalizar programa")


def pedir_opcion() -> int:
    """
    
    """
    mostrar_menu()
    opcion = None
    while opcion is None:
        opcion = pedir_num("Introduce opción (1-3): ")
        if opcion not in OPCIONES_VALIDAS:
            print(f"**ERROR** La opción {opcion} no existe.")
            opcion = None
    return opcion


def ejecutar_opcion(opcion: int):
    """
    
    """
    if opcion == 1:
        print(start())
    elif opcion == 2:
        print(imprimir_listado())
    elif opcion == 3:
        print("Hasta pronto!")
        exit()


def start() -> str:
    """
    
    """
    return f"Este es el texto de opcion uno"


def imprimir_listado() -> str:
    """
    
    """
    return f"Esto es el texto de opcion dos"


def main():
    while True:
        opcion = pedir_opcion()

        ejecutar_opcion(opcion)


if __name__ == "__main__":
    main()