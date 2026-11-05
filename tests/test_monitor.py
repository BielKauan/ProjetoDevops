import logging
from urllib.error import HTTPError, URLError
from unittest.mock import patch, MagicMock

from app.monitor import verificar_servico, validar_url, adicionar_url  


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

def test_servico_registra_reposta_sucesso(caplog):
    resposta_falsa = MagicMock()
    resposta_falsa.status = 200

    with patch("app.monitor.urlopen") as urlopen_falso:
        urlopen_falso.return_value.__enter__.return_value = resposta_falsa

        with caplog.at_level(logging.INFO):
            verificar_servico("https://exemplo.com")

    assert "https://exemplo.com | HTTP 200" in caplog.text

def test_requisicao_utiliza_user_agent():
    resposta_falsa = MagicMock()
    resposta_falsa.status = 200

    with patch ("app.monitor.urlopen") as urlopen_falso:
        urlopen_falso.return_value.__enter__.return_value = resposta_falsa

        verificar_servico("https://exemplo.com")

    requisicao = urlopen_falso.call_args.args[0]

    assert requisicao.get_header("User-agent") == "DevOps-Monitor/1.0"
    assert urlopen_falso.call_args.kwargs["timeout"] == 10 


def test_url_valida():
    assert validar_url("https://google.com") is True 
    assert validar_url("http://exemplo.com") is True

def test_url_invalida():
    assert validar_url("google.com") is False
    assert validar_url("ftp://exemplo.com") is False 
    assert validar_url("https://") is False

def test_url_duplicada():
    urls = ["https://exemplo.com"]

    resultado = adicionar_url("https://exemplo.com", urls)

    assert resultado is False
    assert len(urls) == 1

def test_nova_url_cadastrada():
    urls = []

    resultado = adicionar_url("https://google.com", urls)

    assert resultado is True
    assert "https://google.com" in urls

