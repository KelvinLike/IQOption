import time
import logging
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "Importacao"))
from iqoptionapi.stable_api import IQ_Option
import iqoptionapi.global_value as global_value
from iqoptionapi.constants import ACTIVES

# Configuração de Log
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

email = "[EMAIL_ADDRESS]"
password = "[PASSWORD]"

api = IQ_Option(email, password)

print("\n--- Diagnóstico de Conexão ---")
check, reason = api.connect()

if not check:
    print(f"Erro de conexão: {reason}")
    exit()

print("Conectado!")
api.change_balance("PRACTICE")
print(f"Balance ID selecionado: {global_value.balance_id}")

print("\n--- Verificando Ativos ---")
# Forçar atualização de ativos se necessário
api.get_all_init()

asset = "EURUSD"
asset_id = api.get_all_ACTIVES_OPCODE().get(asset)
print(f"Asset: {asset}, ID: {asset_id}")

if not asset_id:
    print("ERRO: Ativo não encontrado no OPCODE!")
    # Listar alguns ativos para debug
    print("Alguns ativos disponíveis:", list(api.get_all_ACTIVES_OPCODE().keys())[:10])

print("\n--- Testando Compra Digital com Log Detalhado ---")
status, res = api.buy_digital(1, asset, "call", 1)
print(f"Resultado Digital: Status={status}, Resposta={res}")

print("\n--- Testando Compra Binária com Log Detalhado ---")
status, res = api.buy(1, asset, "call", 1)
print(f"Resultado Binário: Status={status}, Resposta={res}")

print("\n--- Testando Compra Blitz com Log Detalhado ---")
status, res = api.buy_blitz(1, asset, "call", 30)
print(f"Resultado Blitz: Status={status}, Resposta={res}")

api.logout()
