import requests
import os
from dotenv import load_dotenv

load_dotenv()  # reads the .env file and loads variables from it

api_key = os.getenv("WEATHER_API_KEY")  # safely grab the key, never typed directly here

city = "London"

response = requests.get(
    "https://api.openweathermap.org/data/2.5/weather",
    params={
        "q": city,
        "appid": api_key,      # <-- this is the authentication part
        "units": "metric"      # so we get Celsius, not Kelvin
    }
)

print("Status code:", response.status_code)
data = response.json()

if response.status_code == 200:
    print(f"City: {data['name']}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Feels like: {data['main']['feels_like']}°C")
    print(f"Weather: {data['weather'][0]['description']}")
else:
    print("Error:", data)