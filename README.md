<div align="center">

<br/>

```
██╗██████╗ ██╗███████╗
██║██╔══██╗██║██╔════╝
██║██████╔╝██║███████╗
██║██╔══██╗██║╚════██║
██║██║  ██║██║███████║
╚═╝╚═╝  ╚═╝╚═╝╚══════╝
```

# Íris — Consultora Financeira com IA

> *"Clareza financeira para cada decisão, em cada momento."*

[![DIO Lab](https://img.shields.io/badge/DIO-Lab%20Bia%20do%20Futuro-8A2BE2?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0xMiAyQzYuNDggMiAyIDYuNDggMiAxMnM0LjQ4IDEwIDEwIDEwIDEwLTQuNDggMTAtMTBTMTcuNTIgMiAxMiAyem0tMiAxNWwtNS01IDEuNDEtMS40MUwxMCAxNC4xN2w3LjU5LTcuNTlMMTkgOGwtOSA5eiIvPjwvc3ZnPg==)](https://github.com/digitalinnovationone/dio-lab-bia-do-futuro)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white)]()
[![IA Generativa](https://img.shields.io/badge/IA-Generativa-f59e0b?style=flat-square)]()
[![Licença](https://img.shields.io/badge/Licença-MIT-64748b?style=flat-square)]()

</div>

---

## 🌟 Sobre o Projeto

**Íris** é um agente de inteligência artificial desenvolvido como consultora financeira pessoal. Seu propósito é democratizar o acesso à orientação financeira de qualidade — oferecendo análises claras, recomendações personalizadas e respostas confiáveis, sem jargões e sem alucinações.

Este repositório é o resultado do lab **"Bia do Futuro"** da [Digital Innovation One (DIO)](https://www.dio.me), onde o desafio é projetar, documentar e implementar um agente financeiro inteligente do zero.

---

## ✨ Capacidades da Íris

| Capacidade | Descrição |
|---|---|
| 📊 **Análise de Perfil** | Identifica o perfil de investidor (conservador, moderado, arrojado) |
| 💡 **Consultoria de Investimentos** | Recomenda produtos financeiros alinhados ao perfil e aos objetivos |
| 🎯 **Planejamento de Metas** | Auxilia na definição e acompanhamento de metas financeiras |
| ⚠️ **Alertas Inteligentes** | Detecta padrões de gastos e emite alertas preventivos |
| 🛡️ **Respostas Confiáveis** | Arquitetura anti-alucinação com base de conhecimento curada |

---

## 🗂️ Estrutura do Projeto

```
dio-lab-bia-do-futuro/
│
├── 📄 README.md
│
├── 📁 data/                        # Base de conhecimento e dados mockados
│   ├── historico_atendimento.csv   # Histórico de atendimentos
│   ├── perfil_investidor.json      # Perfis de clientes
│   ├── produtos_financeiros.json   # Catálogo de produtos disponíveis
│   └── transacoes.csv              # Histórico de transações
│
├── 📁 docs/                        # Documentação completa do agente
│   ├── 01-documentacao-agente.md   # Caso de uso e arquitetura
│   ├── 02-base-conhecimento.md     # Estratégia de dados e RAG
│   ├── 03-prompts.md               # Engenharia de prompts
│   ├── 04-metricas.md              # Avaliação e métricas de desempenho
│   └── 05-pitch.md                 # Roteiro do pitch
│
├── 📁 src/                         # Código-fonte da aplicação
│   └── app.py                      # Ponto de entrada da aplicação
│
└── 📁 assets/                      # Imagens e diagramas
```

---

## 🏗️ Arquitetura

```
┌─────────────────────────────────────────────────────┐
│                    Usuário / Cliente                  │
└──────────────────────────┬──────────────────────────┘
                           │ Input (texto / voz)
                           ▼
┌─────────────────────────────────────────────────────┐
│                    Interface (Chat)                   │
└──────────────────────────┬──────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────┐
│                   Íris — Agente IA                    │
│                                                       │
│   ┌─────────────┐       ┌───────────────────────┐    │
│   │  Engenharia │──────▶│    LLM (Modelo Base)  │    │
│   │  de Prompts │       └───────────┬───────────┘    │
│   └─────────────┘                   │                 │
│                                     ▼                 │
│   ┌─────────────────────────────────────────────┐    │
│   │          Base de Conhecimento (RAG)          │    │
│   │  perfil_investidor · produtos · transações   │    │
│   └─────────────────────────────────────────────┘    │
└──────────────────────────┬──────────────────────────┘
                           │ Resposta validada
                           ▼
                    ✅ Usuário recebe
               consultoria confiável
```

---

## 📚 Documentação do Agente

A pasta `docs/` contém a documentação completa organizada em cinco etapas:

### `01 — Documentação do Agente`
Define o **caso de uso** central da Íris: fornecer consultoria financeira acessível e personalizada. Detalha a **persona** (tom consultivo, empático e objetivo), o público-alvo e o fluxo de interação do agente.

### `02 — Base de Conhecimento`
Descreve a **estratégia de dados**: quais fontes alimentam o agente, como os dados são estruturados (CSV e JSON) e como a abordagem RAG *(Retrieval-Augmented Generation)* garante respostas fundamentadas e evita alucinações.

### `03 — Engenharia de Prompts`
Documenta os **system prompts**, exemplos de few-shot e as instruções de segurança que moldam o comportamento da Íris — incluindo o que ela deve e não deve responder.

### `04 — Métricas de Avaliação`
Define os critérios de qualidade: **precisão das respostas**, taxa de alucinação, satisfação do usuário (CSAT) e tempo médio de resolução — com metas e metodologia de medição.

### `05 — Pitch`
Roteiro para apresentação do projeto: problema, solução, diferenciais da Íris, demonstração ao vivo e próximos passos.

---

## 🚀 Como Executar

### Pré-requisitos

- Python 3.11+
- Chave de API de um LLM (OpenAI, Anthropic, etc.)

### Instalação

```bash
# Clone o repositório
git clone https://github.com/finusz/dio-lab-bia-do-futuro.git
cd dio-lab-bia-do-futuro

# Crie e ative o ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt

# Configure as variáveis de ambiente
cp .env.example .env
# Edite o .env com sua chave de API
```

### Execução

```bash
python src/app.py
```

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Siga os passos:

1. Faça um **fork** do projeto
2. Crie sua branch: `git checkout -b feat/minha-melhoria`
3. Commit suas mudanças: `git commit -m 'feat: adiciona nova funcionalidade'`
4. Push para a branch: `git push origin feat/minha-melhoria`
5. Abra um **Pull Request**

---

## 📄 Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.

---
