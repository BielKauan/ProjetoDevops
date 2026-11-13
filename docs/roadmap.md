# Roadmap — DevOps Service Monitor

**Projeto:** DevOps Service Monitor  
**Versão:** 1.0  
**Status:** Em desenvolvimento

## 1. Objetivo

Documentar as etapas de evolução do DevOps Service Monitor, organizando as funcionalidades implementadas, as atividades em andamento e os próximos objetivos técnicos.

## 2. Etapas do desenvolvimento

### Etapa 1 — Desenvolvimento da aplicação Python

**Status:** Concluída

- Implementação do monitoramento de serviços web.
- Cadastro e validação de URLs.
- Prevenção de URLs duplicadas.
- Tratamento de erros HTTP e falhas de conexão.
- Registro de eventos em arquivos de log.
- Monitoramento contínuo.

### Etapa 2 — Testes automatizados

**Status:** Concluída

- Configuração do Pytest.
- Implementação de testes automatizados.
- Validação dos principais comportamentos da aplicação.
- Execução de nove testes com sucesso.

### Etapa 3 — Conteinerização com Docker

**Status:** Concluída

- Criação do Dockerfile.
- Configuração de múltiplos estágios (test e runtime).
- Criação do arquivo .dockerignore.
- Execução dos testes dentro de um contêiner.
- Execução da aplicação em contêiner.
- Persistência dos logs utilizando volume.

### Etapa 4 — Integração contínua com GitHub Actions

**Status:** Próxima etapa

- Estudar os conceitos de CI e pipelines.
- Criar um workflow utilizando GitHub Actions.
- Automatizar a execução dos testes com Pytest.
- Integrar a validação do projeto ao GitHub.
- Verificar a execução automática dos testes a cada atualização do repositório.

### Etapa 5 — Infraestrutura como código com Terraform

**Status:** Planejada

- Estudar os fundamentos de Infrastructure as Code (IaC).
- Conhecer os principais recursos do Terraform.
- Criar configurações para provisionamento de infraestrutura.
- Versionar os arquivos de infraestrutura.
- Aplicar e testar configurações em ambiente controlado.

### Etapa 6 — Integração com Cloud

**Status:** Planejada

- Estudar os fundamentos de computação em nuvem.
- Avaliar serviços de Cloud adequados ao projeto.
- Planejar uma implantação com atenção aos custos.
- Publicar a aplicação em um ambiente de nuvem.
- Documentar a arquitetura e o processo de implantação.

### Etapa 7 — Segurança e boas práticas

**Status:** Planejada

- Estudar gerenciamento seguro de variáveis e segredos.
- Analisar vulnerabilidades nas dependências.
- Aplicar o princípio do menor privilégio.
- Avaliar ferramentas de análise de segurança.
- Explorar práticas de DevSecOps.

## 3. Objetivo final

Construir um projeto de portfólio que demonstre conhecimentos práticos em Python, testes automatizados, Docker, Git, GitHub Actions, Terraform, Cloud e fundamentos de segurança.

O desenvolvimento será incremental, com documentação e versionamento das alterações realizadas em cada etapa.
