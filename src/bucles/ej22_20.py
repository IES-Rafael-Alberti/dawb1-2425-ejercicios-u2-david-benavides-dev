# Ejercicio 2.2.20
# Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase). Recorrer la frase, carácter a carácter, comparando con la letra buscada. 
# Si el carácter no coincide, indicar que no hay coincidencia en esa posición (imprimiendo la posición) y continuar. 
# Si se encuentra una coincidencia, indicar en qué posición se encontró y finalizar la ejecución.


def buscar_letra_palabra(frase: str, letra_introducida: str) -> str:
    """
    
    """
    for i, letra in enumerate(frase):
        if letra != letra_introducida:
            print(f"No hay coincidencia en la posición {i}.")
        else:
            print(f"Coincidencia encontrada en la posición {i}.")
            exit()


def main():
    frase = input("Ingrese una frase: ")
    letra_introducida = input("Ingrese una letra: ")

    buscar_letra_palabra(frase, letra_introducida)


if __name__ == "__main__":
    main()