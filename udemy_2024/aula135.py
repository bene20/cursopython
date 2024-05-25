import os
pessoa=dict(nome='Ana', idade=25)
carro=dict(fabricante='Fiat', ano=1970)

completo={**pessoa, **carro}

print(pessoa)
print(carro)
print(completo)

os.system('clear')
config={
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
}

def mostraargs(**kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)

mostraargs(**config)

def mostraargs2(kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)

mostraargs2(config)        