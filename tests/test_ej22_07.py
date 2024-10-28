import pytest
from src.bucles.ej22_07 import *


@pytest.mark.parametrize(
    "num, expected",
    [
        (5, "5 x 0 es: 0\n5 x 1 es: 5\n5 x 2 es: 10\n5 x 3 es: 15\n5 x 4 es: 20\n5 x 5 es: 25\n5 x 6 es: 30\n5 x 7 es: 35\n5 x 8 es: 40\n5 x 9 es: 45\n5 x 10 es: 50"),
        (4, "4 x 0 es: 0\n4 x 1 es: 4\n4 x 2 es: 8\n4 x 3 es: 12\n4 x 4 es: 16\n4 x 5 es: 20\n4 x 6 es: 24\n4 x 7 es: 28\n4 x 8 es: 32\n4 x 9 es: 36\n4 x 10 es: 40"),
    ]
)
def test_tabla_multiplicar_numero_params(num, expected):
    assert tabla_multiplicar_numero(num) == expected