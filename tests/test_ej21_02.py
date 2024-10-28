import pytest
from src.condicionales.ej21_02 import *


password_default = "Asdf12345"


@pytest.mark.parametrize(
    "password_usuario, expected",
    [
        ("Asdf12345", True),
        ("SDFsadf54xcc", False),
    ]
)
def test_coincide_password_params(password_usuario, expected):
    assert coincide_password(password_usuario) == expected


@pytest.mark.parametrize(
    "mock_input, expected",
    [
        ("Password ", "Password"),
        (" Password ", "Password"),
        (" Password ", "Password"),
    ]
)
def test_obtener_password_params(mock_input, expected, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: mock_input)
    assert obtener_password() == expected


@pytest.mark.parametrize(
    "obtener_pass, expected",
    [
        ("Asdf12345", "Tu contraseña 'Asdf12345' coincide con la contraseña guardada en la variable."),
        ("SDFsadf54xcc", "Tu contraseña 'SDFsadf54xcc' NO coincide con la contraseña guardada en la variable."),
    ]
)
def test_mostrar_password_params(obtener_pass, expected):
    assert mostrar_password(obtener_pass) == expected