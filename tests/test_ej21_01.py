import pytest
from src.condicionales.ej21_01 import *


@pytest.mark.parametrize(
    "mock_input, expected",
    [
        ("8", 8),
        ("5", 5),
        ("6", 6),
    ]
)
def test_obtener_edad_params(mock_input, expected, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: mock_input)
    assert obtener_edad() == expected


@pytest.mark.parametrize(
    "edad, expected",
    [
        (15, False),
        (18, True),
    ]
)
def test_mostrar_edad_params(edad_validada, expected):
    assert mostrar_edad(edad_validada) == expected


@pytest.mark.parametrize(
    "edad_validada, expected",
    [
        (15, "Tienes 15 años y eres menor de edad."),
        (18, "Tienes 18 años y eres mayor de edad."),
    ]
)
def test_mostrar_edad_params(edad_validada, expected):
    assert mostrar_edad(edad_validada) == expected