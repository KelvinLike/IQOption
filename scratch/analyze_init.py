import json

with open("init_data_debug.json", "r") as f:
    data = json.load(f)

print("--- BINARY ---")
for aid, info in data.get("binary", {}).get("actives", {}).items():
    if "EURUSD" in info.get("name", ""):
        print(f"ID: {aid}, Name: {info.get('name')}, Enabled: {info.get('enabled')}")

print("\n--- TURBO ---")
for aid, info in data.get("turbo", {}).get("actives", {}).items():
    if "EURUSD" in info.get("name", ""):
        print(f"ID: {aid}, Name: {info.get('name')}, Enabled: {info.get('enabled')}")

print("\n--- DIGITAL ---")
for aid, info in data.get("digital", {}).get("actives", {}).items():
    if "EURUSD" in info.get("name", ""):
        print(f"ID: {aid}, Name: {info.get('name')}, Enabled: {info.get('enabled')}")

print("\n--- BLITZ ---")
for aid, info in data.get("blitz", {}).get("actives", {}).items():
    if "EURUSD" in info.get("name", ""):
        print(f"ID: {aid}, Name: {info.get('name')}, Enabled: {info.get('enabled')}")
