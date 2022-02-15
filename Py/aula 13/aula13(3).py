import requests

response= requests.get("https://viacep.com.br")
print(response.status_code)
print(type(response.json()))