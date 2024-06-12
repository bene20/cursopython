
def testelista2(nome, lista=[]):
    lista.append(nome)
    return lista

def testelista(nome, lista=None):
    if lista is None:
        lista=[]
    lista.append(nome)
    return lista

cli1 = testelista('Ana')
cli2 = testelista('Beto')

print(f'{cli1=}, {cli2=}')