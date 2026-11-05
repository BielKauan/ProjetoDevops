import logging
import time 

from urllib.request import Request, urlopen 
from urllib.error import URLError, HTTPError
from urllib.parse import urlparse


logging.basicConfig(
    filename="monitor.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding="utf-8"
)

def validar_url(url):
    endereco = urlparse(url)

    return endereco.scheme in ("http", "https") and bool(endereco.netloc)

def adicionar_url(url, urls):
    if url in urls:
        return False

    urls.append(url)
    return True 

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

    except (URLError, TimeoutError) as erro:
        print(f"URL: {url}")
        print("Resultado: Falha na conexão com o servidor")
        print(f"Detalhes: {erro}")

        logging.error(f"{url} | Falha de conexão: {erro}")


if __name__ == "__main__":
    print("=== DEVOPS SERVICE MONITOR ===")

    urls = []

    while True:
        url = input("\nDigite uma URL (ou 'iniciar' para continuar, 'sair' para encerrar): ").strip()

        if url.lower() == "sair":
            print("Monitoramento encerrado.")
            raise SystemExit

        if url.lower() == "iniciar":
            if not urls:
                print("Erro: cadastre pelo menos uma URL.")
                continue
            break

        if not url:
            print("Erro: Você precisa informar uma URL.")
            continue

        if not validar_url(url):
            print("Erro: informe uma URL válida, começando com http:// ou https://.")
            continue

        if url in urls:
            print("Essa URL já foi cadastrada!")
            continue 
        urls.append(url)
        print(f"URL cadastrada: {url}")

    print("\nURLs cadastradas:")
    for item in urls:
        print(f"- {item}")

    print("\nEscolha o modo de monitoramento:")
    print("1 - Monitoramento único")
    print("2 - Monitoramento contínuo")

    modo = input("\nDigite sua opção: ").strip()

    if modo == "1":
        print("\nIniciando monitoramento único...\n")
        for item in urls:
            verificar_servico(item)

    elif modo == "2":
        print("\nIniciando monitoramento contínuo... (Ctrl+C para parar)\n")
        try:
            while True:
                for item in urls:
                    verificar_servico(item)
                print("\nAguardando 30 segundos...\n")
                time.sleep(30)
        except KeyboardInterrupt:
            print("\nMonitoramento encerrado.")

    else:
        print("Opção inválida.")