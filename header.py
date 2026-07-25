import requests
import os

token = "test123456"  # temporary fake value just to see it work, no real API needed yet

headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.get("https://httpbin.org/headers", headers=headers)

print("Status code:", response.status_code)
print(response.json())