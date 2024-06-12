# nomearquivo='meudocumento.txt'

# with open(nomearquivo, 'w+') as arquivo:
#     arquivo.write('Linha 1\n')
#     arquivo.seek(0,0)
#     print(arquivo.readline())

with open('meudocumento2.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.writelines(
        ('Ação Linha 1\n', 'Ação Linha 2\n', 'Ação Linha 3\n')
    )

with open('meudocumento2.txt', 'r') as arquivo:
    for linha in arquivo.readlines():
        print(linha.strip())


# with open(nomearquivo, 'w') as arquivo:
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')

# with open(nomearquivo, 'r') as arquivo:
#     print(arquivo.readline())
