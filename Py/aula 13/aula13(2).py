import requests

response= requests.get("https://viacep.com.br")
print(response.text)