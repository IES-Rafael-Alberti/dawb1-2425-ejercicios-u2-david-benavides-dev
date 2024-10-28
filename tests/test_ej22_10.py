import pytest
from src.bucles.ej22_10 import *


@pytest.mark.parametrize(
    "num, expected",
    [
        (5, True),
        (10, False),
        (1, False),
        (0, False),
        (-5, False)
    ]
)
def test_validar_primo_params(num, expected):
    assert validar_primo(num) == expected