# Ejercicio 2.3.1
# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).


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


def validar_edad(edad: int) -> bool:
    if edad < 0 or edad > 100:
        return False
    return True


def anios_cumplidos(edad: int) -> str:
    serie_edad = ""
    for i in range(edad+1):
        serie_edad = f"{(serie_edad)} + {i}"
    return serie_edad[3:]


def mostrar_serie_edad(edad) -> str:
    serie_edad = anios_cumplidos(edad)
    return f"Para llegar a tu edad actual ({edad}) has tenido que cumplir {serie_edad} años."
    

def main():
    edad = pedir_num("Introduce tu edad: ")

    while validar_edad(edad) is False:
        edad = pedir_num("Introduce una edad correcta: ")

    print(mostrar_serie_edad(edad))


if __name__ == "__main__":
    main()