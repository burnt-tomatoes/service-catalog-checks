import requests
import os
import base64
import json

token = os.getenv("SERVICE_CATALOG_TOKEN")
payload = os.getenv("PAYLOAD")
payload = base64.b64decode(payload).decode('utf-8')
payload = json.loads(payload)
print("Received payload of:", payload)
url = payload["server"]["url"] + payload["server"]["endpoint"]
if payload["check"]["slug"] == "nope":
  data = {"result": "fail"}
else:
  data = {"result": "pass"}
headers = {"Authorization": f"Token {token}"}
print("Calling", url, "with", data)
res = requests.patch(url, data, headers=headers)
print("Response", res.status_code)
