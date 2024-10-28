# Ejercicio 2.2.25
# Solicitar al usuario que ingrese una frase y luego informar cuál fue la palabra más larga (en caso de haber más de una, mostrar la primera) y cuántas palabras había. 
# Precondición: se tomará como separador de palabras al carácter “ “ (espacio), ya sea uno o más.


frase = input("Introduce una frase: ")

frase = frase.split()


palabra_mas_larga = ""
contar_palabras = 0


for palabra in frase:
    if len(palabra) > len(palabra_mas_larga):
        palabra_mas_larga = palabra
    contar_palabras += 1

print(palabra_mas_larga)
print(contar_palabras)


def main():
    return


if __name__ == "__main__":
    main()