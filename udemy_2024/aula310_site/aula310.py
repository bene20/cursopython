import requests

url = 'http://localhost:3333/'

response = requests.get(url)
print(type(response), response.status_code, response.headers, sep='\n')
#print('Corpo da Resposta:', response.text, sep='\n')