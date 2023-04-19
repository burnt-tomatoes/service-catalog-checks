import requests
import os
import base64
import json

token = os.getenv("SERVICE_CATALOG_TOKEN")
payload = os.getenv("PAYLOAD")
payload = base64.b64decode(payload).decode('utf-8')
payload = json.loads(payload)
url = payload["server"]["url"] + payload["server"]["endpoint"]
data = {"result": "pass"}
headers = {"Authorization": f"Token {token}"}
requests.post(url, data, headers=headers)
