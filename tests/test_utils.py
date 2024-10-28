import pytest
from src.bucles.utils import validar_num, validar_num_positivo


@pytest.mark.parametrize(
    "numero, expected",
    [
        ("123", True),
        ("-123", True),
        ("0", True),
        ("abc", False),
        ("12.34", False),
        ("", False)
    ]
)
def test_validar_num(numero, expected):
    assert validar_num(numero) == expected


@pytest.mark.parametrize(
    "numero, expected",
    [
        ("123", True),
        ("1", True),
        ("0", False),
        ("-1", False),
        ("abc", False),
        ("", False)
    ]
)
def test_validar_num_positivo(numero, expected):
    assert validar_num_positivo(numero) == expected