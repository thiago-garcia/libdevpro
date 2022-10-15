from libdevpro.spam.enviador_de_email import Enviador
from libdevpro.spam.main import EnviadorDeSpam


def test_qde_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar(
        'thiago-garcia@outlook.com',
        'Curso DevPro',
        'Confira os módulos fantásticos'
    )
