# Ejercicio 2.2.23
# Crear un programa que permita al usuario ingresar títulos de libros por teclado, finalizando el ingreso al leerse el string “*” (asterisco). 
# Cada vez que el usuario ingrese un string de longitud 1 que contenga sólo una barra (“/”) se considera que termina una línea. 
# Por cada línea completa, informar cuántos dígitos numéricos (del 0 al 9) aparecieron en total (en todos los títulos de libros que componen en esa línea). 
# Finalmente, informar cuántas líneas completas se ingresaron.
# Ejemplo de ejecución:
# Libro: Los 3 mosqueteros
# Libro: Historia de 2 ciudades
# Libro: /
# Línea completa. Aparecen 2 dígitos numéricos.
# Libro: 20000 leguas de viaje submarino
# Libro: El señor de los anillos
# Libro: /
# Línea completa. Aparecen 5 dígitos numéricos.
# Libro: 20 años después
# Libro: *
# Fin. Se leyeron 2 líneas completas.


DIGITOS = "1234567890"


def contar_numeros(libro: str, cont = 0) -> int:
    for DIGITOS in libro:
        cont += 1
    return cont


def pedir_libros(libro = None, lista_libro = "") -> str:
    while libro != "*":
        libro = input("Libro: ")
        if libro == "/":
            lista_libro = libro
            print(f"Linea completa. Aparecen {contar_numeros(lista_libro)} dígitos numéricos.")
    pass


def main():
    pedir_libros()


if __name__ == "__main__":
    main()