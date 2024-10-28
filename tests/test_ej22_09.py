import pytest
from src.bucles.ej22_09 import *


password = "at90sIVTJW4fX"


@pytest.mark.parametrize(
    "pass_user, expected",
    [
        ("3465dsgf6547", False),
        ("at90sIVTJW4fX", True),
    ]
)
def test_comparar_password_params(pass_user, expected):
    assert comparar_password(pass_user) == expected


@pytest.mark.parametrize(
    "mock_input, expected",
    [
        (["wrong_pass", "at90sIVTJW4fX"], "Bienvenido."),
        (["wrong_pass", "another_wrong", "at90sIVTJW4fX"], "Bienvenido."),
        (["at90sIVTJW4fX"], "Bienvenido."),
    ]
)
def test_introducir_password(mock_input, expected, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: mock_input.pop(0))
    assert introducir_password("Introduce tu contraseña: ") == expected