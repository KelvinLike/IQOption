import time
import logging
from iqoptionapi.stable_api import IQ_Option

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

email = "testedemo159@gmail.com"
password = "testedemo20"

api = IQ_Option(email, password)
api.connect()
api.change_balance("PRACTICE")

asset = "EURUSD-OTC"
print(f"\n--- Verificando Instrument IDs para {asset} ---")
api.subscribe_strike_list(asset, 1)
time.sleep(5)
data = api.get_realtime_strike_list(asset, 1)
print(f"Strike List keys: {list(data.keys())[:5] if data else 'None'}")
if data:
    # A chave do strike list costuma ser o instrument_id
    example_id = list(data.keys())[0]
    print(f"Exemplo de Instrument ID: {example_id}")

api.unsubscribe_strike_list(asset, 1)
api.logout()
