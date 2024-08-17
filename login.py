import requests

url = 'http://localhost:5000/login'
data = {'username': 'usuario_existente', 'password': 'senha_correta'}

response = requests.post(url, json=data)
print(response.json())
