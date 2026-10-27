from urllib.request import Request, urlopen 
from urllib.error import URLError, HTTPError
from socket import timeout

def verificar_servico(url):
    requisicao = Request(
        url,
        headers={"User-Agent": "DevOps-Monitor/1.0"}
    )
    try:

        with urlopen(requisicao, timeout=10) as resposta:
            print(f"URL: {url}")
            print("Resultado: Serviço resposndeu")
            print(f"Status HTTP: {resposta.status}")

    except (URLError, HTTPError, TimeoutError) as erro:
        print(f"URL: {url}")
        print("Resultado: Serviço respondeu")
        print(f"Status HTTP: {resposta.status}")

    except HTTPError as erro:
        print(f"URL: {url}")
        print("Resultado: Servidor retornou erro HTTP")
        print(f"Status HTTP: {erro.code}")


if __name__=="__main__":
    servicos = ["http://www.google.com","https://www.github.com", "https://www.python.org" 
    ]

    for servico in servicos:
        verificar_servico(servico)
        print("-" * 40)