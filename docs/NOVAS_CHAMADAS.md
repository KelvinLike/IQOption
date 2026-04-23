# Guia de Atualizações e Novas Chamadas (API IQ Option v5)

Este documento detalha como utilizar as novas funcionalidades e correções aplicadas na biblioteca `iqoptionapi`, incluindo o suporte completo a Opções Digitais, Opções Blitz e a correção definitiva do fluxo de dados no `get_candles` em cenários multi-thread.

---

## 1. Múltiplas Threads Seguras (`get_candles`)

O método `get_candles` foi totalmente refatorado para suportar execuções assíncronas concorrentes sem a necessidade de instanciar múltiplos objetos `IQ_Option`. O gargalo global (_Race Condition_) foi removido.

**Uso Antigo (Sofria com concorrência):**
Se duas threads executassem `get_candles` no mesmo exato momento, elas poderiam bloquear umas às outras e misturar os dados (uma thread de EURUSD poderia acabar recebendo os dados do GBPUSD).

**Uso Atual (100% Thread-safe):**
Você pode criar 10 threads para 10 ativos diferentes e todas usarão o mesmo método simultaneamente. Cada pedido ganha um ID único (Request ID), impedindo qualquer cruzamento ou vazamento de dados.

```python
import threading
from iqoptionapi.stable_api import IQ_Option
import time

api = IQ_Option("email", "senha")
api.connect()

def worker(ativo):
    # Pode ser chamado simultaneamente por centenas de threads!
    velas = api.get_candles(ativo, 60, 5, time.time())
    print(f"{ativo}: {velas[0]['close']}")

# Ambas as chamadas rodarão em paralelo, independentes uma da outra:
t1 = threading.Thread(target=worker, args=("EURUSD",))
t2 = threading.Thread(target=worker, args=("GBPUSD",))

t1.start()
t2.start()
```

---

## 2. Negociando Opções Digitais (Nova Versão 3.0)

A estrutura interna de chamadas de Digitais foi atualizada. O servidor da IQ Option mudou a forma como os ativos Digitais são lidos e as posições são compradas, exigindo a "versão 3.0" da interface de comunicação. Além disso, a biblioteca agora auto-corrige o nome do ativo internamente, identificando quando usar sufixos como `-op` ou `-OTC`.

**Exemplo de Compra Digital:**
A função permanece inalterada na superfície, mas a estabilidade interna foi reescrita.

```python
ativo = "EURUSD"
valor = 1.0 # 1 Dólar/Real
direcao = "call" # ou "put"
duracao = 1 # 1 minuto, 5 minutos, 15 minutos

# Verifica se o mercado está aberto
isOpen = api.check_win_digital_v2(ativo)
if isOpen:
    # A API lidará com a conversão (ex: EURUSD-op, EURUSD-OTC) automaticamente.
    id_compra, id_ordem = api.buy_digital_spot_v2(ativo, valor, direcao, duracao)
    print(f"Ordem enviada: {id_ordem}")
```

---

## 3. Negociando Opções Blitz (Hyper-reduzidas)

As **Opções Blitz** (que operam na janela hiper-reduzida de expiração) utilizam a versão `"2.0"` do core de envio de expirações. Elas possuem tempos não convencionais em que você indica a quantidade de segundos corridos (como 30s) na frente.

**Exemplo de Compra Blitz (30 Segundos):**
A função para executar compras no formato Blitz usa o `buy_multi`.

```python
ativo = "EURUSD"
valor = 1.0
direcao = "call" # ou "put"
tempo_expiracao = 30 # Segundos (Apenas tempos suportados pelo formato Blitz do ativo atual)

status, id_ordem = api.buy_multi(valor, direcao, ativo, tempo_expiracao, "blitz")

if status:
    print(f"Ordem Blitz enviada com sucesso: ID {id_ordem}")
else:
    print(f"Falha ao enviar ordem Blitz: {id_ordem}")
```
*(Nota: Para ordens Blitz, a IQ Option impõe restrições pesadas de latência. Enviar ordens muito pertos do encerramento da vela resultará no erro de 'Suspensão de Trading').*

---

## 4. Otimização de Diagnóstico de Ativos

Para fins de inspeção (debug), todos os 3 instrumentos agora são carregados automaticamente via websocket no momento da conexão, permitindo descobrir dinamicamente se um mercado está aberto pela detecção de subjacentes.

Para listar todos os ativos suportados:
```python
# Retorna True se a conexão foi inicializada e todos os mercados abertos.
print(api.ALL_Asset) # Ativos Normais / Binárias / Turbo
```

## Conclusão

Todas essas alterações rodam debaixo dos panos. A grande vantagem dessa atualização é que você não precisa reaprender novos métodos, apenas voltar a utilizar os seus robôs normalmente, desfrutando de uma conexão inquebrável por _race conditions_ e um core de mercado (Binária, Digital e Blitz) plenamente compatível com os servidores de 2026.
