
import functools

produtos=[
    {'nome': 'Produto 1', 'preco': 10.00},
    {'nome': 'Produto 3', 'preco': 17.50},
    {'nome': 'Produto 2', 'preco':  1.00},
    {'nome': 'Produto 6', 'preco': 22.00},
    {'nome': 'Produto 5', 'preco': 30.25},
    {'nome': 'Produto 4', 'preco': 11.00},
]

# produtos_reajustados = map(
#     lambda p : {**p,'preco': round(p['preco']*1.1,2)},
#     produtos
# )

# print(*produtos, sep='\n')
# print()
# print(*list(produtos_reajustados), sep='\n')

# produtos_caros = filter(
#     lambda p : p['preco'] > 10,
#     produtos
# )

# print(*produtos, sep='\n')
# print()
# print(*list(produtos_caros), sep='\n')

valortotal = functools.reduce (
    lambda t, p : t + p['preco'],
    produtos,
    0
)

print(valortotal)
