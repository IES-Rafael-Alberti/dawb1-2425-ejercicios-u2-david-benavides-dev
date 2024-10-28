# Ejercicio 2.2.7
# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.


def pedir_num_positivo(msg) -> int:
    """
    
    """
    numero = None
    while numero == None:
        numero = input(msg)
        if validar_num_positivo(numero):
            return int(numero)
        else:
            print("**ERROR** Debes introducir un número entero positivo")
            numero = None


def validar_num_positivo(numero: str) -> bool:
    """
    
    """
    try:
        int(numero)
        return int(numero) > 0
    except ValueError:
        return False


def tabla_multiplicar_numero(num: int):
    """
    
    """
    tabla_multiplicar = ""
    for i in range(1, 10+1):
        tabla_multiplicar += f"{num} x {i} es: {(i * num)}\n"
    return tabla_multiplicar.rstrip("\n")


def main():
    num = pedir_num_positivo("Introduce un número: ")
    print(tabla_multiplicar_numero(num))


if __name__ == "__main__":
    main()