from unittest.mock import Mock
import pytest
from libdevpro.spam.main import EnviadorDeSpam
from libdevpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Thiago', email='thiago@email.com'),
            Usuario(nome='Felipe', email='felipe@email.com')
        ],
        [
            Usuario(nome='Thiago', email='thiago@email.com'),
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'thiago-garcia@outlook.com',
        'Curso DevPro',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Thiago', email='thiago@email.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'felipe@outlook.com',
        'Curso DevPro',
        'Confira os módulos fantásticos'
    )
    enviador.enviar.assert_called_once_with == (
        'felipe@outlook.com',
        'thiago@email.com',
        'Curso DevPro',
        'Confira os módulos fantásticos'
    )
