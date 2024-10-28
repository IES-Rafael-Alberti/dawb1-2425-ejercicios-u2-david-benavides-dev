# Ejercicio 2.2.20
# Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase). Recorrer la frase, carácter a carácter, comparando con la letra buscada. 
# Si el carácter no coincide, indicar que no hay coincidencia en esa posición (imprimiendo la posición) y continuar. 
# Si se encuentra una coincidencia, indicar en qué posición se encontró y finalizar la ejecución.


def main():
    frase = input("Ingrese una frase: ")
    buscar_letra = input("Ingrese una letra: ")

    for i, letra in enumerate(frase):
        if letra != buscar_letra:
            print(f"No hay coincidencia en la posición {i}.")
        else:
            print(f"Coincidencia encontrada en la posición {i}.")
            exit()

if __name__ == "__main__":
    main()