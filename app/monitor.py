import logging
from urllib.request import Request, urlopen 
from urllib.error import URLError, HTTPError
from socket import timeout
from urllib.parse import urlparse

logging.basicConfig(
    filename="monitor.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding="utf-8"
)

def verificar_servico(url):
    requisicao = Request(
        url,
        headers={"User-Agent": "DevOps-Monitor/1.0"}
    )
    try:

        with urlopen(requisicao, timeout=10) as resposta:
            print(f"URL: {url}")
            print("Resultado: Serviço respondeu")
            print(f"Status HTTP: {resposta.status}") 

            logging.info(f"{url} | HTTP {resposta.status}")

    except HTTPError as erro:
        print(f"URL: {url}")
        print("Resultado: Serviço retornou erro HTTP")
        print(f"Status HTTP: {erro.code}")

        logging.error(f"{url} | HTTP {erro.code}")

    except (URLError, TimeoutError, timeout) as erro:
        print(f"URL: {url}")
        print("Resultado: Falha na conexão com o servidor")
        print(f"Detalhes: {erro}")

        logging.error(f"{url} | Falha de conexão: {erro}")


if __name__=="__main__":
    print("=== DEVOPS SERVICE MONITOR ===")


    while True:
        url = input("\nDigite uma URL (ou 'sair' para encerrar): ")

        if url.lower() == "sair":
            print("Monitoramento encerrado.")
            break

        if not url:
            print("Erro: Você precisa informar uma URL.")
            continue 
        
        endereco = urlparse(url)

        if endereco.scheme not in ("http", "https") or not endereco.netloc:
            print("Erro: informe uma URL válida, começando com http:// ou https://.")

        verificar_servico(url)
        print("-" * 40)