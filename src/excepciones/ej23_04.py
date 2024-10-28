# Ejercicio 2.3.4
# Escribir un programa que pida al usuario un número entero, si la entrada no es correcta, mostrará el mensaje "La entrada no es correcta" y lanzará la excepción capturada.


def pedir_num_positivo(msg) -> int:
    numero = None
    while numero == None:
        numero = input(msg)
        if validar_num_positivo(numero):
            return int(numero)
        else:
            numero = None


def validar_num_positivo(numero: str) -> bool:
    try:
        int(numero)

        if int(numero) <= 0:
            raise ValueError("El número debe ser mayor que 0.")
        return True
    except ValueError as e:
        print(f"La entrada no es correcta. Código de error -> {e}")
        return False


def main():
    pedir_num_positivo("introduce un numero: ")


if __name__ == "__main__":
    main()