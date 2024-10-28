# Ejercicio 2.2.12
# Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.


def pedir_palabra(msj: str) -> str:
    """
    
    """
    palabra = input(msj).strip()
    return palabra


def pedir_letra(msj: str, letra_valida = None) -> str:
    """
    
    """
    while letra_valida is None:
        letra = str(input(msj)).strip()
        if len(letra) != 1 or not letra.isalpha():
            print("Debes introducir UNA letra.")
            letra_valida = None
        else:
            return letra


def contar_letras(palabra: str, letra: str) -> int:
    """
    
    """
    cont = 0
    for _ in palabra:
        if _.lower() == letra.lower():
            cont += 1
    return cont


def main():

    palabra = pedir_palabra("Introduce una palabra: ")
    letra = pedir_letra("Introduce una letra: ")
    
    print(contar_letras(palabra, letra))


if __name__ == "__main__":
    main()