# Ejercicio 2.2.8 ver 2
# 
# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
# 
# Con par/impar


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

    
def es_par_impar(numero: int) -> bool:
    """
    
    """
    if numero % 2 == 0:
        return True
    else:
        return False


def mostrar_triangulo_rectangulo_numeros(num: int) -> str:
    cont = 1
    serie = ""
    serie_completa = ""

    if es_par_impar(num):
        while cont <= num+1:
            serie = f"{cont-1} " + serie
            cont += 2
            serie_completa += f"{serie}\n"
    else:
        while cont <= num+1:
            serie = f"{cont} " + serie
            cont += 2
            serie_completa += f"{serie}\n"
    return serie_completa.strip()
    

def main():
    num = pedir_num_positivo("Introduce un número: ")
    print(mostrar_triangulo_rectangulo_numeros(num))

if __name__ == "__main__":
    main()