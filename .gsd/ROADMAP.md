# ROADMAP.md

> **Current Phase**: Not started
> **Milestone**: v1.0 - Estabilização e Atualização

## Must-Haves (from SPEC)
- [x] Correção multi-thread `get_candles`.
- [ ] Operações Binárias, Digitais e Blitz funcionais.
- [ ] WebSocket atualizado e estável.

## Phases

### Phase 1: Diagnóstico e WebSocket
**Status**: 🟩 Completed
**Objective**: Validar a conexão atual, atualizar endpoints e estabilizar o core do WebSocket.
**Requirements**: REQ-06
- [x] Criar script de diagnóstico inicial (`diagnostic_test.py`).
- [x] Executar diagnóstico e capturar logs de erro (Mercado Fechado / WebSocket Timeout).
- [x] Corrigir bug de callbacks do WebSocket (on_close/on_error) no `client.py`.
- [x] Atualizar `stable_api.py` para carregar ativos Digitais via `get_digital_underlying`.
- [x] Implementar suporte à chave `blitz` no carregamento de ativos.
- [x] Validar conexão estável pós-correções.

### Phase 2: Correção de Fluxo de Dados (Multi-thread)
**Status**: 🟩 Completed
**Objective**: Corrigir a race condition no `get_candles` e garantir que o estado da API seja thread-safe.
**Requirements**: REQ-04, REQ-05

### Phase 3: Operações e Ativos (Binária/Digital)
**Status**: ⬜ Not Started
**Objective**: Restaurar a funcionalidade de compras Binárias e Digitais e corrigir a detecção de ativos.
**Requirements**: REQ-01, REQ-02, REQ-07

### Phase 4: Implementação Blitz e Validação
**Status**: ⬜ Not Started
**Objective**: Adicionar suporte nativo ao Blitz e realizar testes de estresse finais.
**Requirements**: REQ-03
