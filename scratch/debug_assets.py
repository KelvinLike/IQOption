import time
import logging
from iqoptionapi.stable_api import IQ_Option
import iqoptionapi.global_value as global_value

# Configuração de Log reduzida para focar no essencial
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

email = "testedemo159@gmail.com"
password = "testedemo20"

api = IQ_Option(email, password)

print("\n--- Diagnóstico de Ativos e Opções ---")
check, reason = api.connect()

if not check:
    print(f"Erro de conexão: {reason}")
    exit()

api.change_balance("PRACTICE")

# 1. Verificar Ativos Binários Abertos
print("\n--- Ativos Binários Abertos ---")
all_open = api.get_all_open_time()
binary_open = all_open.get("binary", {})
open_binaries = [k for k, v in binary_open.items() if v.get("open")]
print(f"Total: {len(open_binaries)}")
print(f"Exemplos: {open_binaries[:5]}")

# 2. Verificar Ativos Digitais Abertos
print("\n--- Ativos Digitais Abertos ---")
digital_open = all_open.get("digital", {})
open_digitals = [k for k, v in digital_open.items() if v.get("open")]
print(f"Total: {len(open_digitals)}")
print(f"Exemplos: {open_digitals[:5]}")

# 3. Verificar Ativos Blitz Abertos
print("\n--- Ativos Blitz Abertos ---")
# Blitz costuma aparecer como 'turbo' ou em uma categoria específica
# Vamos olhar o get_instruments('blitz') se existir
try:
    blitz_instruments = api.get_instruments("blitz")
    print(f"Instrumentos Blitz: {len(blitz_instruments) if blitz_instruments else 0}")
except:
    print("Blitz instruments not found via get_instruments")

# 4. Tentar uma compra no primeiro ativo aberto encontrado
if open_digitals:
    ativo = open_digitals[0]
    print(f"\n--- Testando Digital em {ativo} ---")
    status, res = api.buy_digital(1, ativo, "call", 1)
    print(f"Resultado Digital {ativo}: {status} - {res}")
else:
    print("Nenhum ativo Digital aberto no momento.")

if open_binaries:
    ativo = open_binaries[0]
    print(f"\n--- Testando Binário em {ativo} ---")
    status, res = api.buy(1, ativo, "call", 1)
    print(f"Resultado Binário {ativo}: {status} - {res}")

# Testar Blitz explicitamente se soubermos um ativo
# Geralmente Blitz está disponível nos mesmos que Turbo
if open_binaries:
    ativo = open_binaries[0]
    print(f"\n--- Testando Blitz em {ativo} ---")
    status, res = api.buy_blitz(1, ativo, "call", 5)
    print(f"Resultado Blitz {ativo}: {status} - {res}")

api.logout()
