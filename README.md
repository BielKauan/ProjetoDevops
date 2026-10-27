# DevOps Service Monitor

Projeto prático de monitoramento de serviços web desenvolvido em Python, com testes automatizados e integração contínua (CI) usando GitHub Actions.

## Objetivo

Verificar a disponibilidade de serviços web, identificar respostas HTTP e tratar falhas de conexão. O projeto demonstra conceitos fundamentais de automação, testes de software e práticas de DevOps.

## Tecnologias utilizadas

- **Python** — implementação do monitoramento.
- **pytest** — execução de testes automatizados.
- **unittest.mock** — simulação de respostas e falhas durante os testes.
- **Git e GitHub** — versionamento e hospedagem do código.
- **GitHub Actions** — automação da execução dos testes por meio de integração contínua (CI).

## Funcionalidades

- Verificação de serviços por meio de requisições HTTP.
- Identificação de respostas HTTP bem-sucedidas.
- Tratamento de erros HTTP.
- Tratamento de falhas de conexão e timeout.
- Testes automatizados sem depender de falhas reais nos serviços externos.

## Estrutura do projeto

```text
ProjetoDevops/
├── .github/
│   └── workflows/
├── app/
│   └── monitor.py
├── tests/
│   └── test_monitor.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Como executar

### 1. Pré-requisitos

- Python instalado.
- Git instalado, caso deseje clonar o repositório.

### 2. Instalar as dependências

No terminal, na pasta do projeto, execute:

```bash
python -m pip install -r requirements.txt
```

### 3. Executar o monitor

```bash
python -m app.monitor
```

### 4. Executar os testes automatizados

```bash
python -m pytest -v
```

## Integração contínua

O projeto utiliza GitHub Actions para automatizar a execução dos testes. Isso ajuda a identificar problemas no código durante o processo de desenvolvimento.

## Aprendizados

Este projeto faz parte dos meus estudos práticos em DevOps, com foco em Python, automação, testes, controle de versão e integração contínua.

## Próximas melhorias

- Adicionar registro de eventos em arquivos de log.
- Permitir configurar os serviços monitorados.
- Integrar Docker ao projeto.
- Evoluir o pipeline de CI/CD.
