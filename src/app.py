import pandas as pd
import streamlit as st
import json, requests

# ========== configuração ==========
OLLAMA_URL = 'http://localhost:11434/api/generate'
MODELO = 'gpt-oss' #ollama run gpt-oss

# ========== carregar dados ==========
transacoes = pd.read_csv(r'.\data\transacoes.csv')
historico = pd.read_csv(r'.\data\historico_atendimento.csv')
with open(r'.\data\perfil_investidor.json', 'r', encoding='utf-8') as f:
    perfil = json.load(f)
with open(r'.\data\produtos_financeiros.json', 'r', encoding='utf-8') as f:
    produtos = json.load(f)


# ========== montar contexto ==========
contexto = f'''
Cliente: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
Objetivo: {perfil['objetivo_principal']}
Patrimônio: R$ {perfil['patrimonio_total']} | reserva: R$ {perfil['reserva_emergencia_atual']}

Transações recentes:
{transacoes.to_string(index=False)}

Atendimentos anteriores:
{historico.to_string(index=False)}

Produtos disponíveis:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
'''

# ==========  system prompt ==========

system_prompt = '''
Você é iris um consultor financeiro direto, informativo, didático e acessível Que alerta os gastos do usuário.Informando em que estão sendo aplicados, e oferece dicas de como diminuí-los

REGRAS:
1. Sempre baseie suas respostas nos dados fornecidos
2. Nunca invente informações financeiras
3. Se não souber algo, admita e ofereça alternativas de perguntas que você consegue ajudar
4. Não sugerir investimentos
5. Nunca responda perguntas além do escopo financeiro

CONTEXTO:
Utilizar as bases de conhecimento
'''

# ========== chamar ollama ==========
def perguntar(msg):
    prompt = f'''
{system_prompt}

CONTEXTO CLIENTE:
{contexto}

pergunta: {msg}'''
    r = requests.post(OLLAMA_URL, json={'model': MODELO, 'prompt': prompt, 'stream': False})
    return r.json()['response']

# ========== interface ==========
st.title('Iris, sua Consultura Financeira')

if pergunta := st.chat_input('Sua dúvida sobre finanças...'):
    st.chat_message('user').write(pergunta)
    with st.spinner("..."):
        st.chat_message('assistant').write(perguntar(pergunta))
