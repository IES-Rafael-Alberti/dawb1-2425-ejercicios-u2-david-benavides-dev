import pytest
from src.bucles.ej22_03 import *


@pytest.mark.parametrize(
    "numero, expected",
    [
        (5, "1, 3"),
        (10, "1, 3, 5, 7, 9"),
    ]
)
def test_mostrar_impares_params(numero, expected):
    assert mostrar_impares(numero) == expected