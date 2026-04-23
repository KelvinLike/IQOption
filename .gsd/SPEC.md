# SPEC.md — Project Specification

> **Status**: `FINALIZED`

## Vision
Atualizar e estabilizar a biblioteca `iqoptionapi` para suportar as modalidades modernas de negociação (Digital e Blitz) e corrigir falhas críticas de concorrência que impedem o uso confiável em robôs multi-thread.

## Goals
1. **Suporte a Operações:** Garantir o funcionamento estável de entradas em opções Binárias, Digitais e a nova modalidade Blitz.
2. **Correção de Multi-threading:** Resolver o vazamento de dados no método `get_candles`, garantindo que threads diferentes recebam dados dos ativos corretos simultaneamente.
3. **Atualização de Infraestrutura:** Atualizar o cliente WebSocket para as versões mais recentes do protocolo da corretora e melhorar a resiliência da conexão.
4. **Resolução de Erros de Ativos:** Corrigir o erro de "mercado fechado" em pares de moedas que deveriam estar abertos.

## Non-Goals (Out of Scope)
- Desenvolvimento de estratégias de trading automatizadas.
- Criação de interface gráfica (GUI).
- Suporte para outras corretoras.

## Users
Desenvolvedores de robôs de trading (Python) que utilizam a IQ Option como plataforma de execução.

## Constraints
- **Linguagem:** Python 3.x.
- **Protocolo:** WebSocket (WSS) proprietário da IQ Option.
- **Concorrência:** Deve suportar execução multi-thread com uma única instância da API.

## Success Criteria
- [ ] Execução bem-sucedida de ordens Binárias, Digitais e Blitz via código.
- [ ] Teste de estresse multi-thread confirmando que `get_candles` retorna dados independentes por ativo.
- [ ] WebSocket mantendo conexão estável por mais de 24h sem erros de sincronização.
