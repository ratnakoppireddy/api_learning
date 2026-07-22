import requests
import json

response = requests.get("https://api.github.com/repos/facebook/react")
data = response.json()

# Pretty-print the ENTIRE response, nicely formatted, so you can read it
print(json.dumps(data, indent=2))