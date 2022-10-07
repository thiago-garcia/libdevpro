from libdevpro.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


def test_remetente():
    enviador = Enviador()
    resultado = enviador.enviar(
        'thiago-garcia@outlook.com',
        'garciaa.thiago@gmail.com',
        'Cursos DevPro',
        'Curso PyTools'
    )
    assert 'thiago-garcia@outlook.com' in resultado
