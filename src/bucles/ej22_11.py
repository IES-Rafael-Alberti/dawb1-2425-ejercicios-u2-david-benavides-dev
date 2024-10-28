# Ejercicio 2.2.11
# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.


def pedir_palabra(msj: str) -> str:
    """
    
    """
    palabra = input(msj).strip()
    return palabra


def invertir_palabra(palabra: str, letras_invertidas = "") -> str:
    """
    
    """
    for letras in palabra[::-1]:
        letras_invertidas += f"{letras}\n"
    return letras_invertidas.rstrip("\n")


def main():

    palabra = pedir_palabra("Introduce una palabra: ")

    print(invertir_palabra(palabra))


if __name__ == "__main__":
    main()