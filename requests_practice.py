import requests
url = "https://api.github.com"
response = requests.get(url)
print(response.status_code)
print(response.json())
data = response.json()
print(data["current_user_url"])