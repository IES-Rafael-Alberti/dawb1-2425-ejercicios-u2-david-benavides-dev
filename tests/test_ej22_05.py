import pytest
from src.bucles.ej22_05 import *


@pytest.mark.parametrize(
    "cantidad, interes, numero_anios, expected",
    [
        (5, 5, 6, "Año 1: 5.25 €\nAño 2: 5.51 €\nAño 3: 5.79 €\nAño 4: 6.08 €\nAño 5: 6.38 €\nAño 6: 6.70 €"),
        (1, 1, 1, "Año 1: 1.01 €")
    ]
)
def test_calcular_capital_params(cantidad, interes, numero_anios, expected):
    assert calcular_capital(cantidad, interes, numero_anios) == expected