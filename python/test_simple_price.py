import os
import requests

API_KEY = os.getenv("CG_DEMO_API_KEY")
if not API_KEY:
    raise SystemExit("Missing CG_DEMO_API_KEY environment variable")

url = "https://api.coingecko.com/api/v3/simple/price"
params = {"ids": "bitcoin", "vs_currencies": "usd"}
headers = {"x-cg-demo-api-key": API_KEY}

r = requests.get(url, params=params, headers=headers, timeout=30)
r.raise_for_status()
print(r.json())
