import os

caminho = '/home/users/pasta1/pasta2/arquivo.txt'
print(os.path.split(caminho))
print(os.path.splitext(caminho))

print(os.path.dirname(caminho), os.path.basename(caminho))

caminho = '/home/ebenezer.botelho/tmp'
for item in os.walk(caminho):
    print(f'{item=}')
# for root, dir, files in os.walk(caminho):
#     print(f'{root=}\n{dir=}\n{files=}')

print(os.path.expanduser('~/tmp'))