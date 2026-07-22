import requests

# The data we want to SEND to the server
new_user = {
    "name": "Ratnark",
    "email": "rk@example.com",
    "age": 21,
    "address":"cumming",
    "pincode":3132
}

# POST request - notice we pass our data using json=
response = requests.post(
    "https://httpbin.org/post",
    json=new_user
)

print("Status code:", response.status_code)
data = response.json()
print("Server saw this data:", data["json"])