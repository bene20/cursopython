import itertools

#lista=[1,2,3,4,2,1,2,1,3]
#for chave, grupo in itertools.groupby(sorted(lista)):
#    print(chave,' => ', list(grupo))

alunos=[
    {'nome':'Ana', 'nota':'A'},
    {'nome':'Beto', 'nota':'A'},
    {'nome':'Caio', 'nota':'C'},
    {'nome':'Davi', 'nota':'B'},
    {'nome':'Emerson', 'nota':'A'},
    {'nome':'Felipe', 'nota':'C'},
    {'nome':'Joana', 'nota':'A'},
]
chaveordenacao=lambda aluno: aluno['nota']
alunosordenadospornota=sorted(alunos, key=chaveordenacao)
alunosagrupadospornota=itertools.groupby(alunosordenadospornota, key=chaveordenacao)
for chave, grupo in alunosagrupadospornota:
    print(chave,' => ', end='')
    for aluno in grupo:
        print(f'\t{aluno}')