import requests

url = 'http://localhost:5000/register'
data = {'username': 'novo_usuario', 'password': 'nova_senha'}

response = requests.post(url, json=data)
print(response.json())
