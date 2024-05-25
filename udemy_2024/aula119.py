pessoa={
    'nome': 'Bene',
    'sobrenome': 'Perez',
    'nacionalidade': 'Turca',
    'idade': 20
}

print(pessoa)
pessoa.setdefault('nacionalidade', 'brasileira')
print(pessoa)

