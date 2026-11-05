# DevOps Service Monitor

Projeto prático de monitoramento de serviços web desenvolvido em Python, com testes automatizados e integração contínua (CI) utilizando GitHub Actions.

## Objetivo 

Desenvolver uma aplicação capaz de monitorar a disponibilidade de serviços web, identificar respostas HTTP, registrar eventos e tratar falhas de conexão.

O projeto tem como objetivo aplicar conceitos de programação, automação, testes de software e práticas de DevOps.

## Tecnologias utilizadas

- **Python** — desenvolvimento da aplicação.
- **pytest** — execução de testes automatizados.
- **unittest.mock** — simulação de respostas HTTP e falhas durante os testes.
- **Git e GitHub** — versionamento e hospedagem do código.
- **GitHub Actions** — automação dos testes por meio de integração contínua (CI).

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

## Estrutura do projeto 

```text
ProjetoDevops/
├── .github/
│   └── workflows/
├── app/
│   └── monitor.py
├── tests/
│   └── test_monitor.py
├── monitor.log
├── requirements.txt
├── .gitignore
└── README.md
```

## Como executar

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

## Integração contínua (CI)

O projeto utiliza GitHub Actions para executar automaticamente os testes automatizados.

Essa integração permite verificar se as alterações no código mantêm o funcionamento esperado da aplicação.

## Testes automatizados

Atualmente, o projeto possui 9 testes automatizados, cobrindo:

- Disponibilidade de serviços.
- Erros HTTP.
- Falhas de conexão.
- Registro de logs.
- Cabeçalho User-Agent e timeout.
- Validação de URLs.
- Identificação de URLs duplicadas.
- Cadastro de novos endereços.

## Aprendizados

Este projeto faz parte da minha evolução prática na área de tecnologia, com foco em DevOps, automação, Python, testes automatizados, controle de versão e integração contínua.

## Próximas melhorias

- Aprimorar o armazenamento do histórico de monitoramento.
- Integrar Docker para execução em contêineres.
- Implementar infraestrutura como código utilizando Terraform.
- Expandir o pipeline de CI/CD.
- Explorar GitLab CI/CD.
- Desenvolver uma interface web para visualização dos serviços monitorados.

