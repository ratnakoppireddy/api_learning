import requests

response = requests.get("https://api.github.com/repos/facebook/react")

print("Status code:", response.status_code)

if response.status_code == 200:
    data = response.json()  # converts JSON text -> Python dictionary
    print("Forks_count:", data["forks_count"])
    print("Issue _count:", data["open_issues_count"])
    print("created:", data["created_at"])
    print("Htmldata:", data["html_url"])
else:
    print("Something went wrong:", response.json())