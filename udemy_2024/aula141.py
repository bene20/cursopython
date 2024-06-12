produtos = {
    'nome': 'jaca',
    'valor': 20,
    'calorias': 250,
    'tipo': 'fruta'
}

produtos_upper = {
    chave.title() if isinstance(valor, str) else chave: (valor.upper() if isinstance(valor, str) else valor)    
    for chave, valor in produtos.items()
}

print(produtos_upper)

meuset = {i ** 2 for i in range(5)}
print(meuset)