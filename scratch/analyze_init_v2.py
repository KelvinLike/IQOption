import json

try:
    with open("init_data_debug.json", "r") as f:
        data = json.load(f)
    
    print("Keys in init_data:", list(data.keys()))
    
    for key in ["binary", "turbo", "digital", "blitz"]:
        if key in data:
            actives = data[key].get("actives", {})
            print(f"\n--- Actives in {key} ---")
            found_count = 0
            for aid, details in actives.items():
                name = details.get("name", "Unknown")
                enabled = details.get("enabled", False)
                if "EURUSD" in name:
                    print(f"ID: {aid}, Name: {name}, Enabled: {enabled}")
                    found_count += 1
            if found_count == 0:
                print(f"No EURUSD related assets found in {key}")
except Exception as e:
    print(f"Error: {e}")
