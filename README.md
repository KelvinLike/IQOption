# 🚀 IQ Option API v5 - Guia de Instalação e Uso

Bem-vindo ao repositório da **IQ Option API v5**. Esta versão foi refatorada para oferecer maior estabilidade, suporte aos protocolos mais recentes (Digital v3.0 e Blitz v2.0) e correções de bugs críticos da versão legada.

---

## 🛠️ Instalação

Siga os passos abaixo para configurar o ambiente em sua máquina:

1. **Clonar o Repositório**
   ```bash
   git clone <url-do-repositorio>
   cd Importacao
   ```

2. **Criar um Ambiente Virtual (Recomendado)**
   ```bash
   python -m venv venv
   # No Windows:
   .\venv\Scripts\activate
   # No Linux/Mac:
   source venv/bin/activate
   ```

3. **Instalar Dependências**
   ```bash
   pip install -r requirements.txt
   ```

---

## ⚙️ Configuração

1. Localize o arquivo `.env.example` na raiz do projeto.
2. Renomeie-o para `.env`.
3. Preencha suas credenciais:
   ```env
   IQ_EMAIL=seu_email@exemplo.com
   IQ_PASSWORD=sua_senha
   ```

---

## 📖 Como Usar

### 1. Conexão Básica
```python
from iqoptionapi.stable_api import IQ_Option
import os
from dotenv import load_dotenv

load_dotenv()

email = os.getenv("IQ_EMAIL")
password = os.getenv("IQ_PASSWORD")

api = IQ_Option(email, password)
check, reason = api.connect()

if check:
    print("Conectado com sucesso!")
    api.change_balance("PRACTICE") # PRACTICE ou REAL
else:
    print(f"Erro ao conectar: {reason}")
```

### 2. Abrindo Operações

#### **Opções Digitais (v3.0)**
Protocolo atualizado para maior precisão e rapidez.
```python
# Parâmetros: valor, ativo, direção ("call"/"put"), duração (1, 5 ou 15 minutos)
status, order_id = api.buy_digital(1, "EURUSD", "call", 1)
```

#### **Opções Blitz (v2.0)**
Ideal para operações de curtíssimo prazo (segundos).
```python
# Parâmetros: valor, ativo, direção ("call"/"put"), duração em segundos (ex: 5)
status, order_id = api.buy_blitz(1, "EURUSD", "put", 5)
```

#### **Opções Binárias (Legada)**
```python
# Parâmetros: valor, ativo, direção ("call"/"put"), expiração em minutos
status, order_id = api.buy(1, "EURUSD", "call", 1)
```

---

### 3. Outras Funções Úteis

- **Verificar Saldo**:
  ```python
  balance = api.get_balance()
  print(f"Saldo: {balance}")
  ```

- **Trocar entre Real e Treinamento**:
  ```python
  api.change_balance("REAL") # ou "PRACTICE"
  ```

- **Obter Candles (Histórico)**:
  ```python
  # Ativo, Intervalo (segundos), Quantidade, Timestamp final
  candles = api.get_candles("EURUSD", 60, 10, time.time())
  ```

---

## 🔄 Mudanças Principais (v5)

- **Correção de Typos**: Métodos que continham "quites" foram renomeados para "quotes" (ex: `get_instrument_quotes_generated_data`).
- **Remoção de Código Morto**: Limpeza profunda em `stable_api.py` para melhorar a performance.
- **Protocolos Modernos**: Implementação nativa de Digital v3.0 e Blitz v2.0.
- **Estabilidade OTC**: Tratamento aprimorado para ativos OTC (ex: `EURUSD-OTC`).

---

## ⚠️ Dicas e Observações

- **Ativos OTC**: Sempre use o sufixo `-OTC` durante os fins de semana.
- **SSL**: A biblioteca está configurada para suportar ambientes de produção e builds (PyInstaller) sem erros de certificado.
- **Logs**: Você pode ativar o log para debug:
  ```python
  import logging
  logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')
  ```

---

## 🧪 Testando
Para validar sua instalação, execute o script de teste incluído:
```bash
python test_api_v5.py
```

---
*Desenvolvido para traders e desenvolvedores que buscam alta performance na IQ Option.*
