# DevOps Service Monitor

Projeto prático de monitoramento de serviços web desenvolvido em Python, com testes automatizados e execução em contêineres Docker.

O objetivo é aplicar conceitos de programação, automação, testes de software, conteinerização e práticas de DevOps em um projeto real de portfólio.

## Objetivo

Desenvolver uma aplicação capaz de monitorar a disponibilidade de serviços web, identificar respostas HTTP, registrar eventos e tratar falhas de conexão.

O projeto busca demonstrar, na prática, conhecimentos de Python, testes automatizados, Docker, Git e fundamentos de integração e entrega contínuas (CI/CD).

## Tecnologias utilizadas

- **Python 3.14** — desenvolvimento da aplicação.
- **pytest** — execução de testes automatizados.
- **unittest.mock** — simulação de respostas HTTP e falhas durante os testes.
- **Docker** — conteinerização da aplicação.
- **Dockerfile** — definição de imagens para testes e execução.
- **Git e GitHub** — versionamento e hospedagem do código.
- **Linux/Ubuntu (WSL)** — ambiente de desenvolvimento e execução de comandos.

## Funcionalidades

- Monitoramento de serviços por meio de requisições HTTP.
- Identificação de respostas HTTP bem-sucedidas.
- Tratamento de erros HTTP.
- Tratamento de falhas de conexão e timeout.
- Validação de URLs HTTP e HTTPS.
- Bloqueio de URLs duplicadas durante a execução.
- Cadastro de múltiplos serviços.
- Monitoramento único ou contínuo.
- Verificação automática a cada 30 segundos no modo contínuo.
- Registro de eventos em arquivo de log (`monitor.log`).
- Identificação das requisições por meio de User-Agent.
- Execução da aplicação em contêiner Docker.
- Separação entre ambiente de testes e imagem final de execução.

## Estrutura do projeto

```text
ProjetoDevops/
├── app/
│   └── monitor.py
├── tests/
│   └── test_monitor.py
├── Dockerfile
├── .dockerignore
├── .gitignore
├── conftest.py
├── requirements.txt
├── README.md
└── monitor.log (gerado durante a execução)
```

## Como executar localmente

### 1. Pré-requisitos

- Python instalado.
- Git instalado (opcional, caso deseje clonar o repositório).

### 2. Instalar as dependências

No PowerShell, dentro da pasta do projeto:

```powershell
python -m pip install -r requirements.txt
```

### 3. Executar a aplicação

```powershell
python app/monitor.py
```

### 4. Executar os testes automatizados

```powershell
python -m pytest -v
```

## Execução com Docker

O projeto utiliza um Dockerfile com duas etapas (*multi-stage build*), separando o ambiente de testes da imagem final de execução.

Os comandos abaixo devem ser executados no terminal Ubuntu/WSL, dentro da pasta do projeto.

### 1. Construir a imagem de testes

```bash
docker build --target test -t service-monitor:test .
```

Essa etapa instala as dependências de teste e prepara a aplicação e os testes automatizados dentro do contêiner.

### 2. Executar os testes no Docker

```bash
docker run --rm service-monitor:test
```

O contêiner executa os testes automaticamente e é removido após a conclusão.

### 3. Construir a imagem final

```bash
docker build --target runtime -t service-monitor:1.0 .
```

A etapa `runtime` gera uma imagem independente, contendo somente os arquivos necessários para executar a aplicação.

### 4. Executar a aplicação

```bash
docker run --rm -it service-monitor:1.0
```

A aplicação será iniciada no terminal, permitindo cadastrar serviços e escolher o modo de monitoramento.

## Persistência de logs com Docker

Por padrão, os arquivos criados dentro de um contêiner podem desaparecer quando ele é removido.

Para preservar os registros de monitoramento no computador, utilizamos um *bind mount*, compartilhando o arquivo `monitor.log` entre o ambiente local e o contêiner.

Primeiro, crie o arquivo caso ele ainda não exista:

```bash
touch monitor.log
```

Depois, execute:

```bash
docker run --rm -it -v "$PWD/monitor.log:/app/monitor.log" service-monitor:1.0
```

Dessa maneira, os registros gerados pela aplicação dentro do contêiner também ficam disponíveis no arquivo local `monitor.log`.

## Testes automatizados

Atualmente, o projeto possui **9 testes automatizados**, cobrindo:

- Disponibilidade de serviços.
- Erros HTTP.
- Falhas de conexão.
- Registro de logs.
- Cabeçalho User-Agent e timeout.
- Validação de URLs.
- Identificação de URLs duplicadas.
- Cadastro de novos endereços.

Os testes foram executados tanto no ambiente local quanto dentro de um contêiner Docker.

## Integração contínua (CI)

A automação de testes com GitHub Actions está prevista como próxima etapa de desenvolvimento.

A proposta é configurar um pipeline capaz de executar os testes automaticamente e validar a construção das imagens Docker a cada atualização do repositório.

## Aprendizados

Este projeto faz parte da minha evolução prática na área de tecnologia, com foco em DevOps, automação, Python, testes automatizados, controle de versão, Linux e conteinerização.

## Próximas melhorias

- Implementar integração contínua utilizando GitHub Actions.
- Expandir o pipeline para práticas de CI/CD.
- Integrar infraestrutura como código utilizando Terraform.
- Explorar serviços de Cloud Computing para implantação da aplicação.
- Implementar armazenamento estruturado do histórico de monitoramento.
- Explorar práticas de segurança aplicadas ao desenvolvimento e à infraestrutura. 