# Ejercicio 2.2.5
# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
# 
# # Formula para calcular El capital tras un año.
# amount *= 1 + interest / 100
# # En donde:
# # - amount: Cantidad a invertir
# # - interest: Interes porcentual anual 
# Función que solicita entero al usuario.


def pedir_num(msg) -> int:
    """
    
    """
    numero = None
    while numero == None:
        numero = input(msg)
        if validar_num(numero):
            return int(numero)
        else:
            print("**ERROR** Debes introducir un número")
            numero = None


def validar_num(numero: str) -> bool:
    """
    
    """
    try:
        int(numero)
        return True
    except ValueError:
        return False

def pedir_float(msg) -> float:
    """
    
    """
    numero = None
    while numero == None:
        numero = input(msg)
        if validar_float(numero):
            return float(numero)
        else:
            print("**ERROR** Debes introducir un número flotante.")
            numero = None


def validar_float(numero: str) -> bool:
    """
    
    """
    try:
        float(numero)
        return True
    except ValueError:
        return False


def calcular_capital(cantidad: float, interes: float, numero_anios: int):
    """
    
    """
    resultado = ""
    for i in range(1, numero_anios + 1):
        cantidad *= (1 + interes / 100)
        resultado += f"Año {i}: {cantidad:.2f} €\n"
    return resultado.strip()


def main():
    cantidad = pedir_float("Cantidad a invertir: ")
    interes = pedir_float("Interés anual: ")
    numero_anios = pedir_num("Número de años: ")

    print(calcular_capital(cantidad, interes, numero_anios))


if __name__ == "__main__":
    main()