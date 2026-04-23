# Guia de Uso da API Refatorada (iqoptionapi v5)

Este documento descreve as mudanças realizadas na biblioteca `iqoptionapi` e como utilizar as novas chamadas corrigidas e protocolos atualizados.

## 1. Correção de Typos (Quites -> Quotes)

Vários nomes de métodos e atributos que continham o erro de digitação "quites" foram renomeados para "quotes" para manter a consistência técnica.

### Métodos da API (`IQOptionAPI`)
- `subscribe_instrument_quotes_generated()`
- `unsubscribe_instrument_quotes_generated()`

### Atributos da API
- `api.instrument_quotes_generated_data`
- `api.instrument_quotes_generated_timestamp`

### Métodos na `IQOption` (Stable API)
- `get_instrument_quotes_generated_data(ACTIVE, duration)`

---

## 2. Opções Digitais (v3.0)

A implementação de Opções Digitais agora utiliza o protocolo v3.0, proporcionando maior estabilidade.

### Exemplo:
```python
from iqoptionapi.stable_api import IQ_Option

api = IQ_Option("email", "senha")
api.connect()

# Parâmetros: valor, ativo, direção ("call"/"put"), duração (1, 5, 15)
status, order_id = api.buy_digital(1, "EURUSD", "call", 1)

if status:
    print(f"Ordem Digital aberta! ID: {order_id}")
else:
    print(f"Erro: {order_id}")
```

---

## 3. Opções Blitz (v2.0)

As opções Blitz são operações binárias de curtíssimo prazo que utilizam o protocolo mais recente.

### Exemplo:
```python
# Parâmetros: valor, ativo, direção ("call"/"put"), duração em segundos (ex: 5)
status, order_id = api.buy_blitz(1, "EURUSD", "put", 5)

if status:
    print(f"Ordem Blitz aberta! ID: {order_id}")
```

---

## 4. Remoção de Módulos Obsoletos

Foram removidos componentes que causavam instabilidade ou estavam fora de uso:
- **HTTP Loginv2**: Removido em favor do `Login` padrão.
- **Buyback**: Removido. Vendas são tratadas por `sell_option` e `sell_digital_option`.
- **Código Morto**: Grandes blocos de comentários e funções órfãs em `stable_api.py` e `api.py` foram eliminados.

---

## 5. Observações Importantes

1. **Ativos OTC**: Sempre utilize o sufixo `-OTC` (ex: `EURUSD-OTC`).
2. **Ativos Abertos**: A API tenta encontrar o sufixo `-op` automaticamente se necessário, mas o nome padrão (ex: `EURUSD`) é o recomendado.
3. **SSL**: A verificação de SSL está configurada para ignorar erros de hostname em ambientes de build (PyInstaller).
