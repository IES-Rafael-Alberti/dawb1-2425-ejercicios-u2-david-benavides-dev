# Ejercicio 2.2.22
# Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el 0. Por cada número, informar cuántos dígitos pares
# y cuántos impares tiene. 
# Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.


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
        return int(numero) >= 0
    except ValueError:
        return False


def validar_par_impar(numero: int) -> bool:
    """
    
    """
    if numero % 2 == 0:
        return True
    else:
        return False


def calcular_pares_impares_lista(numero: bool = None, pares = 0, impares = 0) -> tuple:
    while numero != 0:
        numero = pedir_num_positivo("Introduce un número positivo: ")
        if validar_par_impar(numero):
            pares += 1
        else:
            impares += 1
    return pares, impares


def main():
    pares, impares = calcular_pares_impares_lista()

    print(f"Números pares introducidos: {pares}\nNúmeros impares introducidos: {impares}")


if __name__ == "__main__":
    main()