# Ejercicio 2.1.10
# 
# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
# 
# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# 
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. 
# Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. 
# Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
from utils import *

# Listas con ingredientes
ingredientes_vegetarianos = ["Pimiento", "Tofu"]
ingredientes_no_vegetarianos = ["Peperoni", "Jamón", "Salmón"]
ingredientes_default =  ["Tomate", "Mozzarella"]

OPCIONES_VEG = "vegetariana", "veg"
OPCIONES_NO_VEG = "no vegetariana", "no veg"


def preguntar_tipo_pizza(respuesta: str) -> bool:
    """
    
    """
    # True vegetariano
    # False No vegetariano
    
    if respuesta in OPCIONES_VEG:
        return True
    elif respuesta in OPCIONES_NO_VEG:
        return False


def mostrar_ingredientes(tipo_de_pizza: bool) -> str:
    """
    
    """
    print(f"Puedes elegir SOLO UNO de los siguientes ingredientes para tu pizza: ")
    if tipo_de_pizza is True:
        for i in ingredientes_vegetarianos:
            print(i)
    elif tipo_de_pizza is False:
        for i in ingredientes_no_vegetarianos:
            print(i)


def escoger_ingrediente(opcion: str, tipo_pizza: bool) -> list:
    """
    
    """

    ingredientes_pizza = list(ingredientes_default)

    if tipo_pizza:
        if opcion in ingredientes_vegetarianos:
            ingredientes_pizza.append(opcion)
            return ingredientes_pizza
    else:
        if opcion in ingredientes_no_vegetarianos:
            ingredientes_pizza.append(opcion)
            return ingredientes_pizza

    return ingredientes_default


def mostrar_pizza(tipo_pizza, ingredientes_pizza) -> str:
    """
    
    """
    if tipo_pizza is True:
        tipo_pizza = "vegetariana"
    else:
        tipo_pizza = "no vegetariana"

    return f"Tu pizza {tipo_pizza} lleva {', '.join(ingredientes_pizza)}."


def menu():
    """
    
    """
    print("Bienvenido a la pizzeria Bella Napoli")
    print("Tenemos dos tipos de pizza: Vegetariana y No vegetariana")
    print(f"TODAS las pizzas de nuestra carta llevan {ingredientes_default[0]} y {ingredientes_default[1]}.")
    print(f"Las pizzas veganas pueden llevar unos ingredientes u otros")
    print(f"Solo puedes escoger un ingrediente extra para cada tipo de pizza.")


def main():
    """
    
    """
    clear()
    menu()
    tipo_de_pizza = None
    while tipo_de_pizza is None:
        tipo_de_pizza = input("Introduce el tipo de pizza que deseas: ").strip().lower()
        if preguntar_tipo_pizza(tipo_de_pizza) is True:
            tipo_de_pizza = preguntar_tipo_pizza(tipo_de_pizza)
            clear()
            print("Has escogido una pizza vegetariana.")
            mostrar_ingredientes(tipo_de_pizza)

            opcion = input("¿Qué ingrediente deseas añadir a tu pizza?: ").strip().capitalize()
            ingredientes = escoger_ingrediente(opcion, tipo_de_pizza)
            print(mostrar_pizza(tipo_de_pizza, ingredientes))

        elif preguntar_tipo_pizza(tipo_de_pizza) is False:
            tipo_de_pizza = preguntar_tipo_pizza(tipo_de_pizza)
            clear()
            print("Has escogido una pizza no vegetariana.")
            mostrar_ingredientes(tipo_de_pizza)

            opcion = input("¿Qué ingrediente deseas añadir a tu pizza?: ").strip().capitalize()
            ingredientes = escoger_ingrediente(opcion, tipo_de_pizza)
            print(mostrar_pizza(tipo_de_pizza, ingredientes))

        else:
            print("Esa pizza no existe.")
            tipo_de_pizza = None


if __name__ == "__main__":
    main()