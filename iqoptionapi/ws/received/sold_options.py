"""Module for IQ option websocket."""

def sold_options(api, message):
    if message["name"] == "sold-options":
        api.sold_options_respond = message
        try:
            for id_number, data in message["msg"].items():
                api.listinfodata.set(data["win"], data["game_state"], int(id_number))
        except:
            pass