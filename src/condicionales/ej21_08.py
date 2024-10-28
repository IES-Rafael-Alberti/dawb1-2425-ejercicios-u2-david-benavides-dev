# Ejercicio 2.1.8
# 
# En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, 
# traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. 
# A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.
# Nivel 	Puntuación
# Inaceptable 	0.0
# Aceptable 	0.4
# Meritorio 	0.6 o más
# 
# Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.
from utils import *


default_puntuacion = 2400

niveles_validos = [0.0, 0.4, 0.6]


def validar_puntuacion(puntuacion: float) -> bool:
    if puntuacion not in niveles_validos and puntuacion < 0.6:
        return False
    return True


def obtener_puntuacion(msj: str) -> float:
    puntuacion = pedir_float(msj)
    while not validar_puntuacion(puntuacion):
        puntuacion = pedir_float("**ERROR** Debes introducir una puntuación de 0.0, 0.4, 0.6 o más: ")
    return puntuacion


def definir_nivel(puntuacion: float) -> str:
    if puntuacion == niveles_validos[0]:
        return "Inaceptable"
    elif puntuacion == niveles_validos[1]:
        return "Aceptable"
    else:
        return "Meritorio"


def calcular_dinero_recibido(puntuacion: float) -> float:
    return puntuacion * default_puntuacion


def mostrar_rendimiento(nivel, dinero) -> str:
    return f"Su nivel de rendimiento es {nivel} y vas a recibir {dinero} € euros."


def main():
    puntuacion = obtener_puntuacion("Introduce tu puntuación: ")
    nivel = definir_nivel(puntuacion)

    dinero = calcular_dinero_recibido(puntuacion)

    print(mostrar_rendimiento(nivel, dinero))


if __name__ == "__main__":
    main()