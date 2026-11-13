# Análise de Requisitos — DevOps Service Monitor

**Projeto:** DevOps Service Monitor  
**Versão do documento:** 1.0  
**Status:** Em desenvolvimento

## 1. Visão geral

O DevOps Service Monitor é uma aplicação desenvolvida em Python para monitorar a disponibilidade de serviços web por meio de requisições HTTP e HTTPS.

A aplicação permite cadastrar endereços, verificar suas respostas, identificar falhas de conexão e registrar eventos em arquivos de log.

O projeto também utiliza testes automatizados e Docker para demonstrar práticas de desenvolvimento, automação e conteinerização.

## 2. Objetivo

Desenvolver uma solução de monitoramento de serviços web que permita verificar sua disponibilidade e registrar informações sobre as respostas recebidas, aplicando conceitos de programação, testes automatizados, conteinerização e práticas de DevOps em um projeto prático de portfólio.

## 3. Requisitos funcionais

Os requisitos funcionais descrevem as funcionalidades que o sistema deve oferecer.

- **RF01 — Cadastro de URLs:** permitir que o usuário informe os endereços dos serviços que deseja monitorar.
- **RF02 — Validação de URLs:** verificar se os endereços informados possuem um formato válido.
- **RF03 — Prevenção de duplicidade:** impedir o cadastro repetido de uma mesma URL.
- **RF04 — Verificação de disponibilidade:** realizar requisições HTTP para verificar se os serviços estão respondendo.
- **RF05 — Registro de resultados:** registrar informações das verificações em um arquivo de log.
- **RF06 — Monitoramento contínuo:** permitir verificações periódicas dos serviços.
- **RF07 — Encerramento:** permitir que o usuário encerre o monitoramento.

## 4. Requisitos não funcionais

Os requisitos não funcionais descrevem características técnicas e critérios de qualidade do sistema.

- **RNF01 — Linguagem:** o sistema deve ser desenvolvido em Python.
- **RNF02 — Testabilidade:** as funcionalidades devem possuir testes automatizados.
- **RNF03 — Conteinerização:** a aplicação deve poder ser executada em um contêiner Docker.
- **RNF04 — Organização:** o código deve ser organizado de maneira simples e compreensível.
- **RNF05 — Registro:** os logs devem apresentar data, horário, nível e resultado da verificação.
- **RNF06 — Portabilidade:** a aplicação deve utilizar uma imagem Docker baseada em Python, permitindo execução em diferentes ambientes compatíveis.

## 5. Tecnologias utilizadas

- Python: desenvolvimento da aplicação.
- Pytest: execução dos testes automatizados.
- Docker: conteinerização da aplicação.
- Git e GitHub: versionamento e armazenamento do código.
- Linux (Ubuntu via WSL2): ambiente de desenvolvimento e execução de comandos.

## 6. Escopo do projeto

Nesta etapa, o projeto contempla o monitoramento de serviços web por meio de requisições HTTP, validação de URLs, prevenção de cadastros duplicados, registro de logs e execução em contêiner Docker.

Também contempla testes automatizados para verificar o comportamento da aplicação.

Funcionalidades futuras, como integração com pipelines CI/CD, infraestrutura como código e implantação em ambiente de Cloud, serão desenvolvidas gradualmente e documentadas conforme sua implementação.

## 7. Critérios de aceitação

O projeto será considerado funcional nesta etapa quando:

- O usuário conseguir cadastrar URLs válidas.
- URLs inválidas forem identificadas.
- URLs duplicadas forem rejeitadas.
- A aplicação conseguir verificar a disponibilidade dos serviços.
- Os resultados forem registrados em arquivo de log.
- O monitoramento contínuo puder ser iniciado e encerrado.
- Os testes automatizados forem executados com sucesso.
- A aplicação puder ser executada por meio de uma imagem Docker.

## 8. Situação atual

O projeto já possui a aplicação Python implementada, testes automatizados com Pytest e configuração Docker com estágios separados para testes e execução.

As próximas etapas previstas incluem a implementação de integração contínua com GitHub Actions, estudos de infraestrutura como código com Terraform e uma futura implantação em ambiente de Cloud.
