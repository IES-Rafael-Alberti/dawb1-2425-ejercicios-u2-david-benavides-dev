# Ejercicio 2.2.10
# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.


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


def validar_primo(num) -> bool:
    """
    
    """
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def mostrar_numero(num):
    """
    
    """
    if validar_primo(num):
        return f"El número {num} es primo."
    return f"El número {num} no es primo."


def main():

    num = pedir_num_positivo("Introduce un número: ")

    print(mostrar_numero(num))


if __name__ == "__main__":
    main()