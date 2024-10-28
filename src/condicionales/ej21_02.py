# Ejercicio 2.1.2
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por 
# pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.


password_default = "Asdf12345"


def coincide_password(password_usuario: str) -> bool:
    """
    
    """
    return password_usuario.lower() == password_default.lower()


def obtener_password() -> str:
    """
    
    """
    password = input("Introduce una contraseña: ")
    return password.strip()


def mostrar_password(obtener_pass: str) -> str:
    """

    """
    if coincide_password(obtener_pass):
        return f"Tu contraseña '{obtener_pass}' coincide con la contraseña guardada en la variable."
    else:
        return f"Tu contraseña '{obtener_pass}' NO coincide con la contraseña guardada en la variable."


def main():
    """
    
    """
    password = obtener_password()
    print(mostrar_password(password))


if __name__ == "__main__":
    main()