## Phase 2 Decisions

**Date:** 2026-04-23

### Scope
- Resolver a race condition que faz o método `get_candles` da API misturar dados de ativos em execuções multi-thread.

### Approach
- Chose: Option A - Mapeamento de mensagens via `request_id`.
- Reason: Em vez de usar um lock global com buffer único, cada chamada `getcandles` incluirá um ID único (timestamp + thread_id). O callback do websocket armazenará a resposta em um dicionário usando este ID, e a thread chamadora buscará e consumirá (pop) os dados direcionados somente a ela. Essa abordagem remove o gargalo de bloqueio síncrono e torna a biblioteca 100% thread-safe para este endpoint.

### Constraints
- Retirar o lock aumenta a capacidade simultânea da API de pedir dados. O usuário precisará gerenciar rate limits no nível do robô/estratégia para evitar punições por excesso de requisições enviadas ao servidor simultaneamente.
