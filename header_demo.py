import requests

response = requests.get("https://httpbin.org/get")

print("=== HEADERS YOU SENT (request) ===")
for key, value in response.request.headers.items():
    print(f"{key}: {value}")

print("\n=== HEADERS THE SERVER SENT BACK (response) ===")
for key, value in response.headers.items():
    print(f"{key}: {value}")