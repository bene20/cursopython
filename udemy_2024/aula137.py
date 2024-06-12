produtos = [
    {'nome': 'Jaca', 'valor': 20},
    {'nome': 'Pepino', 'valor': 10},
    {'nome': 'Melão', 'valor': 5},
]

reajuste = [
    {**produto, 'valor': produto['valor'] * 1.05}
    if produto['valor'] <= 10 else {**produto}
    for produto in produtos 
]

print(*reajuste, sep='\n')

string='032656978561320254125365'
separador='.'
tamanhogrupos=3
print(separador.join(
  [
    string[indice:indice+tamanhogrupos]
    for indice in range(0, len(string), tamanhogrupos) 
  ]
))