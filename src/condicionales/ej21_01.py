# Ejercicio 2.1.1
# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
# from utils import *
# def es_mayor(edad) -> bool:
#     """"""
#     if edad >= 18:
#         return True
#     else:
#         return False
# def anios_validos() -> bool:
#     """"""
#     while True:
#         edad = introducir_int_positivo("Introduce tu edad: ")
#         if 1 <= edad <= 100: 
#             return edad
#         else:
#             print("Debes tener entre 1 y 100 años.")
# def main():
#     """"""
#     edad = anios_validos()
#     if es_mayor(edad):
#         print(f"Tienes {edad} años y eres mayor de edad.")
#     print(f"Tienes {edad} años y eres menor de edad.")
# if __name__ == "__main__":
#     main()

##########################################################################################################
##########################################################################################################

# Ejercicio 2.1.1
# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
# Otra forma >>>>


def es_mayor(edad: int) -> bool:
    """
    
    """
    if edad >= 18:
        return True
    else:
        return False

def obtener_edad() -> int:
    """
    
    """
    edad = None
    while edad == None:
        try:
            edad = int(input("Introduce tu edad: "))
            if edad <= 0 or edad > 100:
                print("La edad debe estar entre 1 y 100")
                edad = None
        except ValueError:
            print("Por favor, introduce una edad correcta.")
    return edad


def mostrar_edad(edad_validada: bool) -> str:
    """
    
    """
    if es_mayor(edad_validada):
        return f"Tienes {edad_validada} años y eres mayor de edad."
    else:
        return f"Tienes {edad_validada} años y eres menor de edad."


def main():
    """
    
    """
    edad = obtener_edad()
    print(mostrar_edad(edad))


if __name__ == "__main__":
    main()