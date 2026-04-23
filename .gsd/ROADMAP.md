# ROADMAP.md

> **Current Phase**: Not started
> **Milestone**: v1.0 - Estabilização e Atualização

## Must-Haves (from SPEC)
- [ ] Correção multi-thread `get_candles`.
- [ ] Operações Binárias, Digitais e Blitz funcionais.
- [ ] WebSocket atualizado e estável.

## Phases

### Phase 1: Diagnóstico e WebSocket
**Status**: ⬜ Not Started
**Objective**: Validar a conexão atual, atualizar endpoints e estabilizar o core do WebSocket.
**Requirements**: REQ-06

### Phase 2: Correção de Fluxo de Dados (Multi-thread)
**Status**: ⬜ Not Started
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
