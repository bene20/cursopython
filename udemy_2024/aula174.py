import itertools

#lista1=['Ana', 'Beto', 'Caio', 'Davi']
#print(*list(itertools.combinations(lista1, 2)), sep='\n')

#lista1=['Ana', 'Beto', 'Caio']
#print(*list(itertools.permutations(lista1, 2)), sep='\n')

tamanhos=['P', 'M', 'G']
cores=['Branca', 'Preta', 'Azul']
camisas=itertools.product(cores, tamanhos)
print(*list(camisas), sep='\n')