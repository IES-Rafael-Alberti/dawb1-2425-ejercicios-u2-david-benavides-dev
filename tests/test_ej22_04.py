import pytest
from src.bucles.ej22_04 import *


@pytest.mark.parametrize(
    "numero, expected",
    [
        (10, "10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0"),
        (5, "5, 4, 3, 2, 1, 0"),
    ]
)
def test_mostrar_cuenta_atras_params(numero, expected):
    assert mostrar_cuenta_atras(numero) == expected