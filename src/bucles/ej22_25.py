# Ejercicio 2.2.25
# Solicitar al usuario que ingrese una frase y luego informar cuál fue la palabra más larga (en caso de haber más de una, mostrar la primera) y cuántas palabras había. 
# Precondición: se tomará como separador de palabras al carácter “ “ (espacio), ya sea uno o más.


def pedir_frase(msj: str) -> str:
    """
    
    """
    frase = input(msj)
    return frase.split(" ")


def devolver_palabras(frase: str) -> tuple:
    """
    
    """
    palabra_mas_larga = ""
    numero_palabras = 0

    for palabra in frase:
        if len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga = palabra
        numero_palabras += 1
    return palabra_mas_larga, numero_palabras


def main():
    frase = pedir_frase("Introduce una frase: ")
    palabra_mas_larga, numero_palabras = devolver_palabras(frase)

    print(f"La palabra más larga es {palabra_mas_larga} y la frase tenia un total de {numero_palabras} palabras.")


if __name__ == "__main__":
    main()