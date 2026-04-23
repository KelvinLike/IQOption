"""Module for IQ option websocket."""

def option(api, message):
    if message["name"] == "option":
        request_id = message.get("request_id")
        if request_id:
            if api.buy_multi_option.get(request_id) is None:
                api.buy_multi_option[request_id] = {}
            
            if message["msg"].get("id") is not None:
                api.buy_multi_option[request_id]["id"] = message["msg"]["id"]
                api.result = True
            elif message["msg"].get("message") is not None:
                api.buy_multi_option[request_id]["message"] = message["msg"]["message"]
                api.result = False
            else:
                api.result = False
