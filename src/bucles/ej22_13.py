# Ejercicio 2.2.13
# Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.


def pedir_palabras(frase: str = "", palabra: str = "") -> str:
    """
    
    """
    while palabra != "fin":
        palabra = input("Introduce una palabra: ")
        frase += (f" {palabra}")
    return frase.strip().rstrip(" fin")


def main():
    frase = pedir_palabras()

    print(frase)


if __name__ == "__main__":
    main()