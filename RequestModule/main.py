import requests
from bs4 import BeautifulSoup

url = "https://api.thedogapi.com/v1/breeds/search?q=Samoyed"
response = requests.get(url)
print(response.status_code)
data = response.json()
print(data)

# soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())
#
# for heading in soup.findAll("bread"):
#     print(heading.text)


# url = "https://www.thedogapi.com/"
# data = {
#     "username": 40,
#     "password": 409940
# }
#
# r2 = requests.post(url=url, data=data)
# print(r2.text)
# print(r2.status_code)
