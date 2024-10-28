import pytest
from src.bucles.ej22_02 import *


@pytest.mark.parametrize(
    "edad, expected",
    [
        (8, True),
        (101, False),
        (20, True),
        (0, True),
    ]
)
def test_validar_edad_params(edad, expected):
    assert validar_edad(edad) == expected


@pytest.mark.parametrize(
    "edad, expected",
    [
        (10, "1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10"),
        (5, "1 + 2 + 3 + 4 + 5"),
    ]
)
def test_anios_cumplidos_params(edad, expected):
    assert anios_cumplidos(edad) == expected


@pytest.mark.parametrize(
    "edad, expected",
    [
        (4, "Para llegar a tu edad actual (4) has tenido que cumplir 1 + 2 + 3 + 4 años."),
        (6, "Para llegar a tu edad actual (6) has tenido que cumplir 1 + 2 + 3 + 4 + 5 + 6 años."),
    ]
)
def test_mostrar_serie_edad_params(edad, expected):
    assert mostrar_serie_edad(edad) == expected