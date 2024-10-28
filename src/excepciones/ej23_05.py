# Ejercicio 2.3.5
# Escribir que solicite una contraseña, y si no coincide con la que se tiene, lance la excepción NameError con el mensaje, "Incorrect Password!!"


password = "hola123"


def main():

    user_pass = input("Introduce una contraseña: ")
    if password != user_pass:
        raise NameError("Incorrect password!")
    
    try:
        user_pass == password
    except NameError as e:
        print(e)


if __name__ == "__main__":
    main()