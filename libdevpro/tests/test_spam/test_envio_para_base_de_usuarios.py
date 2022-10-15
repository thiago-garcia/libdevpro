import pytest
from libdevpro.spam.enviador_de_email import Enviador
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
    enviador = Enviador()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar(
        'thiago-garcia@outlook.com',
        'Curso DevPro',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.qtd_emails_enviados
