import logging
import json
from iqoptionapi.stable_api import IQ_Option

# Configurar logging para ver tudo
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

email = "[EMAIL_ADDRESS]"
password = "[PASSWORD]"

api = IQ_Option(email, password)
check, reason = api.connect()

if check:
    print("Conectado com sucesso!")
    
    # Pegar informações de ativos
    init_data = api.get_all_init()
    
    # Salvar em um arquivo para análise
    with open("init_data_debug.json", "w") as f:
        json.dump(init_data, f, indent=4)
    
    print("Dados de inicialização salvos em init_data_debug.json")
    
    # Tentar encontrar EURUSD
    found = False
    for option_type in ["binary", "turbo", "digital", "blitz"]:
        if option_type in init_data:
            actives = init_data[option_type].get("actives", {})
            for aid, data in actives.items():
                if "EURUSD" in data.get("name", ""):
                    print(f"Encontrado {data.get('name')} em {option_type}: ID {aid}")
                    found = True
    
    if not found:
        print("EURUSD não encontrado nos dados de inicialização!")
    
    api.logout()
else:
    print(f"Falha ao conectar: {reason}")
