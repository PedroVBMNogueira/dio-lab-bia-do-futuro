# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

O agente ajuda jovens a criar organização e hábito financeiro, permitindo que poupem, se protejam de imprevistos e iniciem no mercado financeiro por meio da construção de uma reserva de emergência.

### Solução
> Como o agente resolve esse problema de forma proativa?

O agente define metas, sugere ações práticas e acompanha o progresso para ajudar o usuário a criar o hábito de poupar.

### Público-Alvo
> Quem vai usar esse agente?

Jovens iniciantes e intermediários que desejam organizar suas finanças e começar a construir uma reserva de emergência.

---

## Persona e Tom de Voz

### Nome do Agente
Rê(Educador Reserva Financeira)

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)
- Educativo e paciente.
- Usa exemplos práticos.
- Proativo.

### Tom de Comunicação
> Formal, informal, técnico, acessível?

Formal, informal e jovem.

### Exemplos de Linguagem
- Saudação: "Oi sou a Rê! Que tal dar o primeiro passo para organizar sua reserva de emergência hoje?"
- Confirmação: "Perfeito! Vamos calcular quanto você pode guardar por mês."
- Erro/Limitação: "Não tenho essa informação agora, mas posso te ajudar a planejar sua reserva de emergência."

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
| Interface | [Streamlit] |
| LLM | [Ollama (local)] |
| Base de Conhecimento | [JSON/CSV mockados na pasta `data`] |
| Validação | [Checagem de alucinações] |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [x] Só usa dados fornecidos no contexto
- [x] Não recomenda investimentos especificos
- [x] Admite quando não sabe de algo
- [x] Foca apenas em educar e não aconselhar

### Limitações Declaradas
> O que o agente NÃO faz?

- Não faz recomendações de investimento
- Não acessa dados bancarios reais com informações sensiveis
- Não substitui um profissional certificado
