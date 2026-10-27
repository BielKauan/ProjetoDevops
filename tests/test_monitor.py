from unittest.mock import patch, MagicMock
from app.monitor import verificar_servico


def test_servico_disponivel():
    resposta_falsa = MagicMock()
    resposta_falsa.status = 200

    with patch("app.monitor.urlopen") as urlopen_falso:
        urlopen_falso.return_value.__enter__._return_value = resposta_falsa

        verificar_servico("https://exemplo.com")

        urlopen_falso.assert_called_once()