import requests
import os

token = os.getenv("SERVICE_CATALOG_TOKEN")
payload = os.getenv("PAYLOAD")
url = payload["server"]["url"] + payload["server"]["endpoint"]
data = {"result": "pass"}
headers = {"Authorization": f"Token {token}"}
requests.post(url, data, headers=headers)
