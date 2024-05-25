l1=[
    {'nome':'Zelia','idade':24},
    {'nome':'Beto','idade':11},
    {'nome':'Ana','idade':36},
    {'nome':'Caio','idade':7},
    {'nome':'Tiago','idade':13},
    {'nome':'Helio','idade':99},
]

def ordena(item):
    return item['idade']

#l1.sort(key=ordena)
l1.sort(key=lambda i: i['nome'])
print(l1)