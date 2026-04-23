# Documentação das Novas Chamadas (v5)

Esta documentação descreve como utilizar as novas implementações para operações de Opções Digitais e Binárias (Blitz) que utilizam as versões mais recentes do protocolo da IQ Option.

## 1. Opções Digitais (v3.0)

A nova implementação de Opções Digitais utiliza o protocolo v3.0, que é mais estável e rápido.

### Como usar:

```python
from iqoptionapi.stable_api import IQ_Option

Iq = IQ_Option("email", "senha")
Iq.connect()

# Parâmetros:
# amount: valor da operação (ex: 1)
# active: par de moedas (ex: "EURUSD" ou "EURUSD-OTC")
# action: direção ("call" ou "put")
# duration: tempo de expiração em minutos (ex: 1, 5, 15)

status, order_id = Iq.buy_digital(1, "EURUSD", "call", 1)

if status:
    print(f"Ordem Digital aberta com sucesso! ID: {order_id}")
else:
    print(f"Erro ao abrir ordem Digital: {order_id}")
```

---

## 2. Opções Blitz (v2.0)

As opções Blitz são operações binárias de curtíssimo prazo (5 segundos, 30 segundos, etc.). Elas utilizam o protocolo `binary-options.open-option` v2.0.

### Como usar:

```python
# Parâmetros:
# amount: valor da operação (ex: 1)
# active: par de moedas (ex: "EURUSD" ou "EURUSD-OTC")
# action: direção ("call" ou "put")
# duration: duração em segundos (ex: 5, 30)

status, order_id = Iq.buy_blitz(1, "EURUSD", "call", 5)

if status:
    print(f"Ordem Blitz aberta com sucesso! ID: {order_id}")
else:
    print(f"Erro ao abrir ordem Blitz: {order_id}")
```

---

## Observações Importantes:

1. **Ativos OTC**: Para ativos em OTC, sempre utilize o sufixo `-OTC` (ex: `EURUSD-OTC`).
2. **Ativos Abertos**: Para ativos em mercado aberto, a API automaticamente tenta encontrar o sufixo `-op` se necessário, mas o uso do nome padrão (ex: `EURUSD`) é recomendado.
3. **Gerenciamento de Balanço**: Certifique-se de que o `balance_id` correto está selecionado (Real ou Treinamento) antes de realizar as operações.
