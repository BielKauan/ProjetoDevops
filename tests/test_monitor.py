from urllib.error import HTTPError, URLError
from unittest.mock import patch, MagicMock

from app.monitor import verificar_servico


def test_servico_disponivel():
    resposta_falsa = MagicMock()
    resposta_falsa.status = 200

    with patch("app.monitor.urlopen") as urlopen_falso:
        urlopen_falso.return_value.__enter__._return_value = resposta_falsa

        verificar_servico("https://exemplo.com")

        urlopen_falso.assert_called_once()

def test_servico_error_http(capsys):
    erro_http = HTTPError (
        url="http://exemplo.com",
        code=500,
        msg="Erro interno do serviudor",
        hdrs=None,
        fp=None
    )
    with patch("app.monitor.urlopen", side_effect=erro_http):
        verificar_servico("http://exemplo.com")

    saida = capsys.readouterr().out

    assert "Serviço retornou erro HTTP" in saida
    assert "Status HTTP: 500" in saida

def test_servico_falha_conexao(capsys):

    with patch(
        "app.monitor.urlopen",
        side_effect=URLError("Falha de conexão")
    
    ):
        verificar_servico("http://exemplo.com")

    saida = capsys.readouterr().out

    assert "Falha na conexão com o servidor" in saida
    assert "Falha de conexão" in saida 


