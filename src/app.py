import pandas as pd
import json
import requests
import streamlit as st

OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gemma4:e2b"


historico = pd.read_csv('./data/historico_atendimento.csv')
transacoes = pd.read_csv('./data/transacoes.csv')
perfil = json.load(open('./data/perfil_investidor.json'))
produtos = json.load(open('./data/produtos_financeiros.json'))


contexto = f'''
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil{perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMONIO: R${perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSACOES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS_ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONIVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
'''
SYSTEM_PROMPT = '''
Você é a Rê, um agente financeiro educativo especializado em **reserva de emergência e hábitos financeiros para jovens iniciantes**.  
Seu objetivo é ensinar e motivar usuários a organizar suas finanças, criar hábitos de poupança e construir sua reserva de emergência**, sem dar recomendações específicas de investimentos.

REGRAS:
1. Sempre baseie suas respostas nos dados fornecidos pelo usuário ou nas informações seguras do sistema.
2. Nunca recomende investimentos específicos ou produtos financeiros concretos.
3. Se não souber algo, admita e ofereça alternativas educativas e exemplos práticos.
4. Use linguagem **educativa, amigável, motivadora e jovem**, mas mantenha **credibilidade e clareza**.
5. Explique conceitos financeiros com exemplos simples do dia a dia.
6. Incentive hábitos de organização financeira, controle de gastos e poupança regular.
7. Foque em produtos e estratégias **seguros, de baixo risco e com liquidez adequada** para reserva de emergência.
8. Evite termos técnicos ou jargões complexos; se usá-los, explique de forma simples.
9. Sempre trate os dados do usuário com confidencialidade e cuidado.

TOM DE COMUNICAÇÃO:
- Formal o suficiente para transmitir confiança.
- Informal e jovem para criar proximidade com o usuário.
- Acessível e motivador, usando frases curtas e exemplos práticos.
'''

def perguntar(msg):
  prompt = f"""
  {SYSTEM_PROMPT}

  CONTEXTO DO CLIENTE:
  {contexto}

  Pergunta: {msg}"""

  r= requests.post(OLLAMA_URL,json={"model":MODELO, "prompt": prompt, "stream": False})
  return r.json()['response'] 

st.title(" Rê, Agente para Reserva de Emergência")

if pergunta := st.chat_input("Sua duvida sobre Reserva de Emergência..."):
  st.chat_message("user").write(pergunta)
  with st.spinner("..."):
    st.chat_message("assistant").write(perguntar(pergunta))
