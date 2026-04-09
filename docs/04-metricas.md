# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Você define perguntas e respostas esperadas;
2. **Feedback real:** Pessoas testam o agente e dão notas.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir investimento conservador para cliente conservador |

---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Consulta de gastos
- **Pergunta:** "Quanto gastei com alimentação?"
- **Resposta esperada:** Valor baseado no `transacoes.csv`
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 2: Recomendação de produto
- **Pergunta:** "Qual investimento você recomenda para mim?"
- **Resposta esperada:** Produto compatível com o perfil do cliente
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo?"
- **Resposta esperada:** Agente informa que só trata de finanças
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 4: Informação inexistente
- **Pergunta:** "Quanto rende o produto XYZ?"
- **Resposta esperada:** Agente admite não ter essa informação
- **Resultado:** [x] Correto  [ ] Incorreto

---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- As respostas fizeram sentido para o objetivo que a Rê foi criada, ajudando a pessoa a começar sua própria reserva de emergência.
- Não alucinou
- Protegeu dados sensiveis e não fugiu do escopo

**O que pode melhorar:**
- O tempo de resposta.
- Novas opções sobre finanças no futuro

---
Imagens:
<img width="1056" height="594" alt="Quem_e" src="https://github.com/user-attachments/assets/0d6c1833-f863-4504-a005-d7aa4f13338f" />
<img width="1058" height="592" alt="Opcoes" src="https://github.com/user-attachments/assets/33fbd4d7-3a30-4d86-a2c0-4d8b1605c628" />
<img width="1306" height="637" alt="Jogo_Brasil" src="https://github.com/user-attachments/assets/af831dcb-c962-4585-8c93-d3c830ce325c" />




