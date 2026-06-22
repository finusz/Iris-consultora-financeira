# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores |
| `perfil_investidor.json` | JSON | Personalizar recomendações e entender a renda do cliente|
| `produtos_financeiros.json` | JSON | Conhecer os tipos de aplicações que o cliente faz |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente |

> [!TIP]
> **Quer um dataset mais robusto?** Você pode utilizar datasets públicos do [Hugging Face](https://huggingface.co/datasets) relacionados a finanças, desde que sejam adequados ao contexto do desafio.

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Foram adicionados mais dados de transações no arquivo. Pois o foco principal do agente é compreender estas transações.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Seram carregados atráves de código python para ler os arquivos csv e json

```python
import pandas as pd
import json

#csv
historico  = pd.read_csv('data/historico_atendimento.csv')
transacoes  = pd.read_csv('data/transacoes.csv')

#json
with open('data/perfil_investidor.json', 'r'): as f:
  perfil = json.load(f)

with open('produtos_financeiros.json', 'r'): as f:
  produtos = json.load(f)
```

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Para garantir que o agente tenha o melhor contexto possivel, podemos apenas injetar os dados diretamente no prompt. Porém com mais dados, é mais eficiente que os dados sejam carregados dinamicamente.

```text
HISTORICO(data/historico_atendimento.csv):
data,canal,tema,resumo,resolvido
2025-09-15,chat,CDB,Cliente perguntou sobre rentabilidade e prazos,sim
2025-09-22,telefone,Problema no app,Erro ao visualizar extrato foi corrigido,sim
2025-10-01,chat,Tesouro Selic,Cliente pediu explicação sobre o funcionamento do Tesouro Direto,sim
2025-10-12,chat,Metas financeiras,Cliente acompanhou o progresso da reserva de emergência,sim
2025-10-25,email,Atualização cadastral,Cliente atualizou e-mail e telefone,sim

TRANSACOES (data/transacoes.csv):
data,descricao,categoria,valor,tipo
2025-10-01,Salário,receita,5000.00,entrada
2025-10-02,Aluguel,moradia,1200.00,saida
2025-10-03,Supermercado,alimentacao,450.00,saida
2025-10-05,Netflix,lazer,55.90,saida
2025-10-07,Farmácia,saude,89.00,saida
2025-10-10,Restaurante,alimentacao,120.00,saida
2025-10-12,Uber,transporte,45.00,saida
2025-10-15,Conta de Luz,moradia,180.00,saida
2025-10-20,Academia,saude,99.00,saida
2025-10-25,Combustível,transporte,250.00,saida
2025-10-28,Freelance,receita,800.00,entrada
2025-10-29,Cinema,lazer,70.00,saida
2025-10-30,Conta de Água,moradia,95.00,saida
2025-11-01,Salário,receita,5000.00,entrada
2025-11-02,Aluguel,moradia,1200.00,saida
2025-11-03,Supermercado,alimentacao,520.00,saida
2025-11-05,Spotify,lazer,34.90,saida
2025-11-07,Farmácia,saude,120.00,saida
2025-11-10,Restaurante,alimentacao,150.00,saida
2025-11-12,Ônibus,transporte,30.00,saida
2025-11-15,Conta de Internet,moradia,120.00,saida
2025-11-18,Investimento,receita,300.00,entrada
2025-11-20,Academia,saude,99.00,saida
2025-11-22,Combustível,transporte,270.00,saida
2025-11-25,Show,lazer,200.00,saida
2025-11-28,Freelance,receita,950.00,entrada
2025-11-29,Padaria,alimentacao,35.00,saida
2025-11-30,Transferência Bancária,receita,1500.00,entrada
2025-12-01,Salário,receita,5000.00,entrada
2025-12-02,Aluguel,moradia,1200.00,saida
2025-12-03,Supermercado,alimentacao,480.00,saida
2025-12-04,Manutenção Carro,transporte,600.00,saida
2025-12-05,Disney+,lazer,45.90,saida
2025-12-07,Farmácia,saude,75.00,saida
2025-12-10,Restaurante,alimentacao,200.00,saida
2025-12-12,Taxi,transporte,60.00,saida
2025-12-15,Conta de Gás,moradia,110.00,saida
2025-12-18,Investimento,receita,400.00,entrada
2025-12-20,Academia,saude,99.00,saida
2025-12-22,Combustível,transporte,280.00,saida
2025-12-23,Viagem,lazer,1500.00,saida
2025-12-25,Presente de Natal,lazer,350.00,saida
2025-12-28,Freelance,receita,1200.00,entrada
2025-12-30,Conta de Internet,moradia,130.00,saida
2026-01-01,Salário,receita,5000.00,entrada
2026-01-02,Aluguel,moradia,1250.00,saida
2026-01-03,Supermercado,alimentacao,510.00,saida
2026-01-05,Spotify,lazer,34.90,saida
2026-01-07,Farmácia,saude,95.00,saida
2026-01-10,Restaurante,alimentacao,180.00,saida
2026-01-12,Ônibus,transporte,40.00,saida
2026-01-15,Conta de Luz,moradia,190.00,saida
2026-01-18,Investimento,receita,350.00,entrada
2026-01-20,Academia,saude,99.00,saida
2026-01-22,Combustível,transporte,260.00,saida
2026-01-25,Show,lazer,220.00,saida
2026-01-28,Freelance,receita,1000.00,entrada

PERFIL(data/perfil_investidor.json):
{
  "nome": "João Silva",
  "idade": 32,
  "profissao": "Analista de Sistemas",
  "renda_mensal": 5000.00,
  "perfil_investidor": "moderado",
  "objetivo_principal": "Construir reserva de emergência",
  "patrimonio_total": 15000.00,
  "reserva_emergencia_atual": 10000.00,
  "aceita_risco": false,
  "metas": [
    {
      "meta": "Completar reserva de emergência",
      "valor_necessario": 15000.00,
      "prazo": "2026-06"
    },
    {
      "meta": "Entrada do apartamento",
      "valor_necessario": 50000.00,
      "prazo": "2027-12"
    }
  ]
}

PRODUTOS(produtos_financeiros.json):
[
  {
    "nome": "Tesouro Selic",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "100% da Selic",
    "aporte_minimo": 30.00,
    "indicado_para": "Reserva de emergência e iniciantes"
  },
  {
    "nome": "CDB Liquidez Diária",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "102% do CDI",
    "aporte_minimo": 100.00,
    "indicado_para": "Quem busca segurança com rendimento diário"
  },
  {
    "nome": "LCI/LCA",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "95% do CDI",
    "aporte_minimo": 1000.00,
    "indicado_para": "Quem pode esperar 90 dias (isento de IR)"
  },
  {
    "nome": "Fundo Multimercado",
    "categoria": "fundo",
    "risco": "medio",
    "rentabilidade": "CDI + 2%",
    "aporte_minimo": 500.00,
    "indicado_para": "Perfil moderado que busca diversificação"
  },
  {
    "nome": "Fundo de Ações",
    "categoria": "fundo",
    "risco": "alto",
    "rentabilidade": "Variável",
    "aporte_minimo": 100.00,
    "indicado_para": "Perfil arrojado com foco no longo prazo"
  }
]
```

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000

Últimas transações:
- 22/01: Combustível - R$ 260
- 25/01: Show - R$ 220

Total de gastos por categoria:
- Alimentacao: R$2645.0
- Lazer: R$2511.6
- Moradia: R$5675.0
- Saude: R$775.0
- Transporte: R$1835.0
...
```
