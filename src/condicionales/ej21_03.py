# Ejercicio 2.1.3
# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.


def validar_divisor(divisor) -> bool:
    """
    
    """
    if divisor <= 0:
        print("El divisor debe ser mayor que 0.")
        return False
    return True


def obtener_numeros() -> tuple:
    """
    
    """
    num1 = None
    try:
        while num1 == None:
            num1 = float(input("Introduce el dividendo: "))
    except ValueError as e:
        print("Solo acepto números. Código de error -> {e}")
        num1 = None

    num2 = None
    try:
        while num2 == None:
            num2 = float(input("Introduce el divisor: "))
            if validar_divisor(num2) == False:
                num2 = None
    except ValueError as e:
        print("Solo acepto números. Código de error -> {e}")
        num2 = None

    return num1, num2


def realizar_division(num1, num2) -> float:
    """
    
    """
    return num1 / num2


def mostrar_division(num1, num2, division):
    """
    
    """
    return f"El número {num1} dividido por {num2} da un resultado de {division}."


def main():
    """
    
    """
    num1, num2 = obtener_numeros()
    divisor = realizar_division(num1, num2)

    print(mostrar_division(num1, num2, divisor))


if __name__ == "__main__":
    main()