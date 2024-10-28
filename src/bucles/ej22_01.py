# Ejercicio 2.2.1
# Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
from utils import pause


def pedir_palabra(msj: str) -> str:
    """
    
    """
    palabra = None
    while palabra is None:
        palabra = input(msj).strip()
        if not validar_palabra(palabra):
            palabra = None
            print("**ERROR** No has introducido una palabra.")
            pause()
        else:
            return palabra


def validar_palabra(palabra: str) -> bool:
    """
    
    """
    return palabra.isalpha()


def generar_lista_palabra(palabra: str) -> list:
    """
    
    """
    lista_palabras = []
    for _ in range(10):
        lista_palabras.append(palabra)
    return lista_palabras


def mostrar_palabra(lista_palabras: list) -> str:
    """
    
    """
    for palabra in lista_palabras:
        print(palabra)


def main():
    """
    
    """
    palabra = pedir_palabra("Introduce una palabra: ")
    mostrar_palabra(generar_lista_palabra(palabra))


if __name__ == "__main__":
    main()