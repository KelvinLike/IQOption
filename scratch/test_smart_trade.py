import time
import logging
from iqoptionapi.stable_api import IQ_Option

# Configuração de Log
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

email = "testedemo159@gmail.com"
password = "testedemo20"

api = IQ_Option(email, password)
print("--- Conectando ---")
check, reason = api.connect()

if check:
    print("Conectado com sucesso!")
    api.change_balance("PRACTICE")
    
    # 1. Analisar ativos disponíveis
    init_data = api.get_all_init()
    
    def find_active_eurusd():
        for opt_type in ["binary", "turbo", "digital", "blitz"]:
            if opt_type in init_data:
                actives = init_data[opt_type].get("actives", {})
                for aid, data in actives.items():
                    name = data.get("name", "")
                    enabled = data.get("enabled", False)
                    if "EURUSD" in name and enabled:
                        # Extrair o nome limpo (sem o prefixo front.)
                        clean_name = name.replace("front.", "")
                        return clean_name, opt_type
        return None, None

    ativo, tipo_sugerido = find_active_eurusd()
    
    if not ativo:
        print("Nenhum ativo EURUSD (Normal ou OTC) está habilitado no momento.")
        # Tentar pegar qualquer um habilitado para teste
        for opt_type in ["binary", "turbo"]:
            actives = init_data.get(opt_type, {}).get("actives", {})
            for aid, data in actives.items():
                if data.get("enabled"):
                    ativo = data.get("name", "").replace("front.", "")
                    tipo_sugerido = opt_type
                    break
            if ativo: break

    if ativo:
        print(f"Ativo sugerido: {ativo} (Tipo: {tipo_sugerido})")
        valor = 1
        direcao = "call"
        
        # Testar Binário/Turbo
        print(f"\n--- Testando BINÁRIO em {ativo} ---")
        status, result = api.buy(valor, ativo, direcao, 1)
        if status:
            print(f"Sucesso Binário! ID: {result}")
        else:
            print(f"Erro Binário: {result}")
            
        # Testar Digital
        print(f"\n--- Testando DIGITAL em {ativo} ---")
        status, result = api.buy_digital(valor, ativo, direcao, 1)
        if status:
            print(f"Sucesso Digital! ID: {result}")
        else:
            print(f"Erro Digital: {result}")

        # Testar Blitz
        print(f"\n--- Testando BLITZ em {ativo} ---")
        status, result = api.buy_blitz(valor, ativo, direcao, 5)
        if status:
            print(f"Sucesso Blitz! ID: {result}")
        else:
            print(f"Erro Blitz: {result}")
    else:
        print("Nenhum ativo habilitado encontrado para teste.")

    api.logout()
else:
    print(f"Erro ao conectar: {reason}")
