# Ejercicio 2.4.1
# Algoritmo burbuja

a = [8, 3, 1, 19, 14]


def burbuja(a: list) -> list:
    """ 
    Este "algoritmo burbuja" sirve para intercambiar números de menor a mayor dentro de una lista usando dos bucles anidados.

    En cada iteracion comparará cada par de elementos adyecentes y los intercambiará si no están en el orden correcto.
    Seguirá iterando hasta que la lista esté completamente ordenada de menor a mayor.

    Args:
        list(list): Recibe una lista con números para que el algoritmo la ordene.
    Returns:
        list(list): Retorna la lista ordenada.
    """
    for i in range(len(a)):
        for j in range(0, len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def main():
    print(burbuja(a))


if __name__ == "__main__":
    main()