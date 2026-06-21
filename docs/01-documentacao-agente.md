# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

Alerta os gastos do usuário. Informando em que estão sendo aplicados, e oferece dicas de como diminuí-los.

### Solução
> Como o agente resolve esse problema de forma proativa?

Ele utiliza os próprios dados do cliente e informa, de forma simples, através de rótulos em como o dinheiro dele está sendo gasto.  

### Público-Alvo
> Quem vai usar esse agente?

Pessoas sem muito controle financeiro e que não prestam atenção em despesas diárias.

---

## Persona e Tom de Voz

### Nome do Agente
Iris

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

- Direto
- Paciente
- Não ofender o cliente

### Tom de Comunicação
> Formal, informal, técnico, acessível?

- Forma
- Iformativo
- Didático
- Acessível

### Exemplos de Linguagem
- Saudação: Olá, sou Iris. Qual é o problema que você está enfrentando?
- Confirmação: Compreendido. Deixa-me analisar isso.
- Erro/Limitação: Não consigo auxilia-lo com isso no momento, mas caso tenha interesse posso ajuda-lo com...

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Cliente] -->|Mensagem| B[Interface]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | Streamlit |
| LLM | Ollama |
| Base de Conhecimento | JSON/CSV mockados |
| Validação | Checagem de alucinações |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [ ] Apenas dados fornecidos no contexto
- [ ] Não recomendar investimentos financeiros
- [ ] Não realizar comparações de gastos
- [ ] Não sugerir dicas que fogem da realiadade do usuário
- [ ] Admite quando não souber alguma informação

### Limitações Declaradas
> O que o agente NÃO faz?

- NÃO faz recomendações de investimentos financeiros
- NÃO acessa dados bancários sensiveis
