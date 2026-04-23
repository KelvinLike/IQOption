"""Module for IQ option websocket."""

def candles(api, message):
    if message['name'] == 'candles':
        try:
            # Compatibilidade com a nova logica thread-safe por request_id
            req_id = message.get("request_id")
            if req_id:
                if not hasattr(api.candles, "candles_data_dict"):
                    api.candles.candles_data_dict = {}
                api.candles.candles_data_dict[str(req_id)] = message["msg"]["candles"]
            
            # Retrocompatibilidade
            api.candles.candles_data = message["msg"]["candles"]
        except:
            pass