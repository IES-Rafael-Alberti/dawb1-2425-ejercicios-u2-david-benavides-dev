import pytest
from src.bucles.ej22_06 import *


@pytest.mark.parametrize(
    "msj, expected",
    [
        ("123", True),
        ("-123", False),
        ("0", True),
        ("abc", False),
        ("12.34", False),
        ("", False)
    ]
)
def test_validar_entero(msj, expected):
    assert validar_entero(msj) == expected


@pytest.mark.parametrize(
    "mock_input, expected",
    [
        (["123"], 123),
        (["1"], 1),
        (["0"], 0),
        (["-1"], -1),
        (["abc", "123"], 123),
        (["", "123"], 123)
    ]
)
def test_obtener_entero(mock_input, expected, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: mock_input.pop(0))
    assert obtener_entero() == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (5, " \n*\n**\n***\n****"),
        (4, " \n*\n**\n***"),
        (7, " \n*\n**\n***\n****\n*****\n******"),
    ]
)
def test_generar_triangulo_rectangulo(n, expected):
    assert generar_triangulo_rectangulo(n) == expected