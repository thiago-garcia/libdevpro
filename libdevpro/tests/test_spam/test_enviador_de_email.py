import pytest
from libdevpro.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['foo@bar.com', 'thiago-garcia@outlook.com']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'garciaa.thiago@gmail.com',
        'Cursos DevPro',
        'Curso PyTools'
    )
    assert remetente in resultado
