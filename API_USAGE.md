# Guia de Uso da API Refatorada (iqoptionapi v5)

Este documento descreve as funções mais importantes da biblioteca e como utilizá-las para construir seu robô de trading.

---

## 1. Conexão e Sessão

Essenciais para iniciar e manter a comunicação com os servidores da IQ Option.

- **`connect()`**: Realiza a autenticação via WebSocket.
- **`check_connect()`**: Verifica se a conexão ainda está ativa.
- **`connect_2fa(sms_code)`**: Usado para contas com autenticação de dois fatores.
- **`logout()`**: Encerra a sessão com segurança.

```python
from iqoptionapi.stable_api import IQ_Option

api = IQ_Option("email", "senha")
check, reason = api.connect()

if check:
    print("Conectado!")
else:
    if reason == "2FA":
        code = input("Digite o código SMS recebido: ")
        api.connect_2fa(code)
```

---

## 2. Gerenciamento de Conta

Controle de saldo, moedas e troca de ambiente.

- **`get_balance()`**: Retorna o saldo da conta ativa.
- **`change_balance("REAL" ou "PRACTICE")`**: Alterna entre conta real e treinamento.
- **`get_currency()`**: Retorna a moeda da conta (ex: BRL, USD).
- **`reset_practice_balance()`**: Reseta o saldo da conta de treinamento para $10.000.

---

## 3. Consulta de Ativos e Payout

Identificação de mercados abertos e retorno financeiro.

- **`get_all_open_time()`**: Retorna o status de abertura de todos os mercados (Binárias, Digital, Forex, etc).
- **`get_all_profit()`**: Retorna o payout atual para Binárias/Turbo.
- **`get_digital_payout(ativo)`**: Retorna o payout atual para Opções Digitais.
- **`update_ACTIVES_OPCODE()`**: Atualiza internamente os mapeamentos de nomes para IDs de ativos.

---

## 4. Operações de Compra (Trades)

As três formas principais de realizar operações na plataforma.

### **Opções Binárias / Turbo**
```python
# Parâmetros: valor, ativo, direção ("call"/"put"), expiração em minutos
status, id = api.buy(10, "EURUSD", "call", 1)
```

### **Opções Digitais (v3.0)**
Protocolo atualizado para maior estabilidade.
```python
# Parâmetros: valor, ativo, direção ("call"/"put"), expiração (1, 5 ou 15 minutos)
status, id = api.buy_digital(10, "EURUSD", "put", 5)
```

### **Opções Blitz (v2.0)**
Operações de curtíssimo prazo com expiração em segundos.
```python
# Parâmetros: valor, ativo, direção ("call"/"put"), duração em segundos (ex: 5, 10, 30)
status, id = api.buy_blitz(10, "EURUSD", "call", 5)
```

---

## 5. Monitoramento e Fechamento de Ordens

- **`check_win_v4(id)`**: Verifica o resultado de uma ordem Binária (Win/Loss).
- **`check_win_digital_v2(id)`**: Verifica o resultado de uma ordem Digital.
- **`sell_option(id)`**: Vende uma opção Binária antes do vencimento.
- **`sell_digital_option(id)`**: Vende uma opção Digital antes do vencimento.

---

## 6. Dados de Mercado e Real-time (Candles)

### **Histórico de Velas**
```python
# Ativo, Intervalo (segundos), Quantidade, Timestamp final
candles = api.get_candles("EURUSD", 60, 100, time.time())
```

### **Streaming em Tempo Real**
```python
# Inicia a coleta contínua
api.start_candles_stream("EURUSD", 60, 100)

# Acessa os dados a qualquer momento
velas = api.get_realtime_candles("EURUSD", 60)

# Para a coleta
api.stop_candles_stream("EURUSD", 60)
```

---

## 7. Observações Técnicas

1. **Ativos OTC**: Durante fins de semana, adicione o sufixo `-OTC` (ex: `EURUSD-OTC`).
2. **Typos Corrigidos**: Na v5, todos os métodos que usavam "quites" foram corrigidos para "quotes" (ex: `get_instrument_quotes_generated_data`).
3. **SSL**: A verificação SSL está otimizada para ignorar erros de hostname em ambientes compilados (PyInstaller).

---
*Este guia foca nos métodos mais estáveis e testados da versão 5.*
