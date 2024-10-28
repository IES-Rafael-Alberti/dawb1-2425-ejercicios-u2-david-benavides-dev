# Ejercicio 2.1.6
# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres 
# con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
GENERO_VALIDO = 'Mujer', 'Hombre'


def pedir_nombre(msj: str, nombre = None) -> str:
    while nombre is None:
        nombre = input(msj).strip().capitalize()
        if validar_nombre(nombre):
            return nombre
        nombre = None


def validar_nombre(nombre: str) -> bool:
    try:
        if str(nombre) and len(nombre) > 1 and nombre.isalpha():
            return True
        else:
            raise ValueError("El nombre es inválido.")
    except ValueError as e:
        print(e)


def pedir_genero(msj: str, genero = None) -> str:
    while genero is None:
        genero = input(msj).strip().capitalize()
        if validar_genero(genero):
            return genero
        genero = None


def validar_genero(genero: str) -> bool:
    try:
        if genero in GENERO_VALIDO:
            return True
        else:
            raise ValueError("El género no es correcto. Por favor, introduzca hombre o mujer.")
    except ValueError as e:
        print(e)    


def obtener_grupo(nombre: str, genero: str):
    if genero == "Mujer" and "A" <= nombre[0] <= "M":
        return "A"
    elif genero == "Hombre" and "N" <= nombre[0] <= "Z":
        return "A"
    else:
        return "B"


def mostrar_informacion(nombre: str, genero: str, grupo: str) -> str:
    return f"Te llamas {nombre} y tu genero es {genero}. Perteneces al grupo {grupo}."


def main():
    nombre = pedir_nombre("Introduce tu nombre: ")
    genero = pedir_genero("Introduce tu género: ")

    grupo = obtener_grupo(nombre, genero)

    print(mostrar_informacion(nombre, genero, grupo))


if __name__ == "__main__":
    main()