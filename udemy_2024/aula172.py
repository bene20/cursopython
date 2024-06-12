import itertools

lista1=['Ana', 'Beto', 'Caio']
lista2=[2,5,8,10,69]

print(*zip(lista1, lista2))

for i in itertools.count(5,7):
    if i > 100:
        break
    print(i)