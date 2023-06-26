import requests


api_url = f'https://api.github.com/users/1'
response = requests.get(api_url)
print(response.status_code)
file = response.headers["Content-Type"]
print(file)
data = response.json()
print(data)
