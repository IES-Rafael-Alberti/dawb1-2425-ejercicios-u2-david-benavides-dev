# Ejercicio 2.1.4
# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.


def pedir_num() -> int:
    """
    
    """
    numero = None
    while numero == None:
        numero = input("Introduce un número: ")
        if validar_num(numero):
            return int(numero)
        else:
            print("**ERROR** Debes introducir un número")
            numero = None


def validar_num(numero: str) -> bool:
    """
    
    """
    try:
        if int(numero):
            return True
    except ValueError:
        return False


def es_par_impar(num_validado: int) -> bool:
    """
    
    """

    if num_validado % 2 == 0:
        return True
    return False


def mostrar_resultado(num_validado) -> str:
    """
    
    """
    if es_par_impar(num_validado):
        return f"El número {num_validado} es par."
    return f"El número {num_validado} es impar."


def main():
    """
    
    """
    numero = pedir_num()
    print(mostrar_resultado(numero))


if __name__ == "__main__":
    main()