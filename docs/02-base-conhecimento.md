# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Utilização no Agente Rê |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Dar continuidade ao antendimento anterior de forma mais eficiente |
| `perfil_investidor.json` | JSON | Personalizar explicações especificas para cada perfil de cliente |
| `produtos_financeiros.json` | JSON | Sugerir produtos adequados ao perfil de cada cliente  |
| `transacoes.csv` | CSV | Analisar padrão de gastos e da reserva de emergência do cliente |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.
## 1. produtos_financeiros.json
**Objetivo:** adequar os produtos financeiros ao foco do agente Rê, voltado para **reserva de emergência**.

**Mudanças realizadas:**

- **Removidos produtos não ideais para reserva de emergência:**
  - **LCI/LCA** – exige esperar 90 dias para resgate; não serve para emergência imediata.
  - **Fundo Multimercado** – risco médio e rendimento variável; não é ideal para emergência.
  - **Fundo de Ações** – risco alto e volatilidade grande; indicado apenas para longo prazo.

- **Adicionados:**
  - **Poupança** – risco muito baixo, liquidez imediata; ideal para segurança máxima.
  - **Fundo DI / Renda Fixa com liquidez diária** – baixo risco, rendimento próximo ao CDI, liquidez rápida.
  - **CDB de bancos digitais com liquidez diária** – baixo risco (coberto pelo FGC), rendimento melhor que a poupança, alta liquidez.

## 2. transacoes.csv
**Objetivo:** incluir simulação de reserva de emergência no fluxo de transações do usuário.

**Mudanças realizadas:**
- **Inclusão de linha para Reserva de Emergência:**
  - **Descrição:** Reserva de Emergência
  - **Categoria:** poupanca
  - **Tipo:** saida
  - **Valor:** 10% da receita mensal (R$ 500,00)
  - **Data:** mesmo dia do salário (1º do mês), reforçando o hábito de poupar imediatamente

**Objetivo desta alteração:** permitir que o agente Rê **identifique oportunidades de poupança, acompanhe a reserva de emergência e eduque o usuário** sobre hábitos financeiros consistentes.

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

 Os dados podem ser carregados via código conforme documentação ou via prompt.
``` Python
import pandas as pd
import json

historico = pd.read_csv('data/historico_atendimento.csv')
transacoes = pd.read_csv('data/transacoes.csv')

with open('data/perfil_investidor.json','r', encoding = 'utf-8') as f:
  perfil = json.load(f)

with open('data/produtos.json','r', encoding = 'utf-8') as f:
  produtos = json.load(f)
```

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Os dados podem ir do system do prompt para a solução ficar mais simples, pratica e de melhor entendimento. 

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Renda Mensal: R$ 5.000
- Objetivo: Construir reserva de emergência

Transações Principais:
- 01/10: Salário - R$ 5000
- 01/10: Reserva de Emergência - R$ 500
- 02/10: Aluguel - R$ 1200
- 03/10: Supermercado - R$ 450

Produtos Disponiveis:
- Tesouro Selic
- CDB Liquidez Diária
- Poupança
- Fundo DI / Renda Fixa com liquidez diária
- CDB de bancos digitais com liquidez diária 
```
