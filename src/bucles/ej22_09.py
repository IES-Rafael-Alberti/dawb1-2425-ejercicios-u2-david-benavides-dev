# Ejercicio 2.2.9
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.


password = "at90sIVTJW4fX"


def comparar_password(pass_user) -> bool:
    """
    
    """
    return pass_user == password


def introducir_password(msj) -> str:
    """
    
    """
    pass_user = input(msj)
    while comparar_password(pass_user) is not True:
        pass_user = input("La contraseña no coincide. Vuelve a intentarlo: ")
    return f"Bienvenido."


def main():
    print(introducir_password("Introduce tu contraseña: "))


if __name__ == "__main__":
    main()